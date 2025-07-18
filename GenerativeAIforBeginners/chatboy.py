from langchain.text_splitter import RecursiveCharacterTextSplitter
import streamlit as st

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
# Proceso dado por el insructor
# if file is not None:
#    pdf_reader = PdfReader(file)
#    text = ""
#    for page in pdf_reader.pages:
#        text += page.extract_text() # + "\n" # Le falta este salto de línea

# Display the extracted text
# st.write("Extracted Text:")
# st.write(text)

# Optional: Display the text in a text area
# st.text_area("Text from PDF", value=text, height=300)
# from langchain.text_splitter import RecursiveCharacterTextSplitter

# Break the text into chunks
text_splitter = RecursiveCharacterTextSplitter(
    separators="\n", chunk_size=1000, chunk_overlap=150, length_function=len
)
chunks = text_splitter.split_text(text)

# Display the extracted text
st.write("Extracted Text in Chunks:")
st.write(chunks)
