import os
import fitz  # PyMuPDF
from typing import List
from dotenv import load_dotenv  # Load environment variables
from openai import OpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document

# Set API key or raise an error if not set
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    load_dotenv()  # Carga las variables de entorno del archivo .env
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# print("OpenAI API Key:", OPENAI_API_KEY)

# Instantiate OpenAI client
openai_client = OpenAI(api_key=OPENAI_API_KEY)

# =========================================================
# FAISS & Document Loading Setup
# =========================================================
DB_FILE = "./src/rag/.faiss_index"

# Define the GPT model class
model_name = "gpt-3.5-turbo"  # Example model name, can be changed as needed


class GPTModel:
    def __init__(self, model_name=model_name):
        self.model_name = model_name
        # self.embeddings = OpenAIEmbeddings(openai_api_key=api_key)

    def generate_response(self, prompt: str) -> str:
        """Generate a response using the GPT model."""
        completion = openai_client.chat.completions.create(
            model=self.model_name,
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": prompt}]
        )
        return completion.choices[0].message.content


def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract text from a PDF file using PyMuPDF."""
    text = ""
    page_number = 0
    try:
        with fitz.open(pdf_path) as doc:
            for page in doc:
                page_text = page.get_text("text")
                page_number = page.number + 1
                text += page_text + "\n"
            print(f"Extracting text from page {page_number} of {pdf_path}")
    except Exception as e:
        print(f"Error extracting text from {pdf_path}: {e}")
    return text


def load_documents(folder_path: str) -> List[Document]:
    """Load all PDF and TXT from a folder and return a list of Document objects."""
    local_docs = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        print(f"Processing file: {filename}")
        if filename.endswith(".pdf"):
            text = extract_text_from_pdf(file_path)
        elif filename.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as file:
                text = file.read()
        else:
            continue
        if text.strip():
            local_docs.append(Document(page_content=text,
                                       metadata={"source": filename}))
    return local_docs


def create_vector_db(local_docs):  # List[Document]
    """Create a FAISS vector database from a list of Document objects."""
    print("Local docs type:", type(local_docs),
          "with length:", len(local_docs))
    if not local_docs:
        raise ValueError(
            "No documents provided to create the vector database.")
    if os.path.exists(DB_FILE):
        print(f"Database file {DB_FILE} already exists.")
        print("Please delete it before creating a new one.")
        return
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500, chunk_overlap=100)
    docs = text_splitter.split_documents(local_docs)

    # Generating embeddings

    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

    vector_db = FAISS.from_documents(docs, embeddings)

    # Save the vector store to disk
    vector_db.save_local(DB_FILE)
    print(f"Vector database created and saved to {DB_FILE}.")


def load_vector_db():
    """Create a FAISS vector database from documents in the 'documents' folder."""
    if os.path.exists(DB_FILE):
        return FAISS.load_local(DB_FILE, OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY), allow_dangerous_deserialization=True)
    else:
        raise FileNotFoundError(
            f"Database file {DB_FILE} not found. Please create the database first.")


def retrieve_elevant_docs(query: str, k: int = 3) -> List[Document]:
    """Retrieve the top-k relevant documents chunks from FAISS."""
    vector_db = load_vector_db()
    if vector_db:
        results = vector_db.similarity_search(query, k=k)
        return [doc.page_content for doc in results]
    else:
        print("Vector database not found or could not be created.")
        return []


def chat_with_context(query: str, k: int = 3) -> str:
    """Generate a response to the query using retrieved relevant documents as context."""
    relevant_docs = retrieve_elevant_docs(query, k)
    context = "\n\n".join(relevant_docs)

    prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"
    gpt_model = GPTModel()
    response = gpt_model.generate_response(prompt)
    return response


# =========================================================
# Main Execution
# =========================================================
if __name__ == "__main__":
    FOLDER_PATH = "./src/rag/documents"
    # load_dotenv()  # Carga las variables de entorno del archivo .env
    # OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    # print("OpenAI API Key:", OPENAI_API_KEY)

    # Load documents from the 'documents' folder
    documents = load_documents(FOLDER_PATH)

    # Create FAISS database (run only once per dataset)
    create_vector_db(documents)

    while True:
        user_query = input("Enter your query (or 'exit' to quit): ")
        if user_query.lower() == 'exit':
            break
        responseGPT = chat_with_context(user_query)
        if responseGPT:
            print("\n 💬 ChatGPT Response: \n", responseGPT)
        else:
            print("No relevant documents found.")
    print("Exiting the ChatGPT RAG/Chatbot.")
