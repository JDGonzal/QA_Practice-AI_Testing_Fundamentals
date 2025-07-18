from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
import streamlit as st
from dotenv import load_dotenv
import os

# Upload PDF files
st.header("My First Chatbot")

with st.sidebar:
    st.title("Your Documents")
    # Con esto cargamos los archivos PDF
    file = st.file_uploader("Upload a PDF and start asking questions",
                            type="pdf", accept_multiple_files=True)

# Extract the text from the PDF files
if file is not None:
    from PyPDF2 import PdfReader

    text = ""
    for pdf_file in file:
        reader = PdfReader(pdf_file)
        for page in reader.pages:
            text += page.extract_text() + "\n"

# Break the text into chunks
text_splitter = RecursiveCharacterTextSplitter(
    separators="\n", chunk_size=1000, chunk_overlap=150, length_function=len
)
chunks = text_splitter.split_text(text)

# Display the extracted text
# st.write("Extracted Text in Chunks:")
# st.write(chunks)

# Generating embeddings
load_dotenv()  # Carga las variables de entorno del archivo .env
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
print("OpenAI API Key:", OPENAI_API_KEY)
embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)


# Create a vector store - FAISS
vector_store = FAISS.from_texts(chunks, embeddings)
