from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_community.chat_models import ChatOpenAI

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

    if not chunks:
        st.write("No text extracted from the PDF files.")

    if chunks:
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

        # Get user query
        user_question = st.text_input("Ask a question about your documents")

        # Do similarity search
        if user_question:
            results = vector_store.similarity_search(user_question, k=3)
            # results = vector_store.similarity_search(user_question)

            # Display the results
            # st.write("Results:")
            # for result in results:
            #     st.write(result.page_content)

            # define the LLM chain
            llm = ChatOpenAI(
                openai_api_key=OPENAI_API_KEY,
                temperature=0.2,
                max_tokens=1000,
                model_name="gpt-3.5-turbo"
            )

            # Output the answer
            chain = load_qa_chain(llm, chain_type="stuff")
            response = chain.run(input_documents=results,
                                 question=user_question)
            st.write("Answer:")
            st.write(response)
