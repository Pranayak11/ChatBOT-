import os
import streamlit as st
from PyPDF2 import PdfReader
from hashlib import sha256
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA

st.set_page_config(page_title=" AMLGOLABS AI Chatbot", layout="wide")
st.markdown("""
    <style>
        .main { background-color: #f0f4f8; }
        .block-container { padding-top: 2rem; }
        .stButton > button {
            background-color: #1f3b57;
            color: white;
            border-radius: 8px;
            font-weight: bold;
        }
        .stTextInput > div > div > input {
            border-radius: 8px;
            padding: 10px;
            border: 1px solid #ccc;
        }
        .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
            color: #1f3b57;
        }
        .sidebar .sidebar-content {
            background-color: #e3f2fd;
        }
    </style>
""", unsafe_allow_html=True)

st.sidebar.image("AMLGOLOGO.png", width=150)
st.sidebar.title(" AMLGOLABS Chat Assistant")
st.sidebar.markdown("####  Empowering Documents with AI Intelligence")

st.markdown("""
    <div style='text-align: center;'>
        <img src='AMLGO.png' width='120'>
        <h1 style='color: #1f3b57;'>AMLGOLABS - Intelligent Document Chatbot</h1>
        <h4 style='color: #455a64;'>Ask smart questions, get contextual answers — powered by open-source LLMs.</h4>
    </div>
    <hr>
""", unsafe_allow_html=True)

st.markdown("###  Upload Your PDF Document Below")
uploaded_file = st.file_uploader(" Upload PDF File", type="pdf")
if uploaded_file:
    pdf_path = os.path.join("data", "uploaded.pdf")
    os.makedirs("data", exist_ok=True)
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("!! PDF uploaded and processed successfully!")

    reader = PdfReader(pdf_path)
    raw_text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])

    if not raw_text.strip():
        st.error("!! Could not extract any text from the uploaded PDF.")
        st.stop()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    docs = splitter.create_documents([raw_text])

    unique_docs = []
    seen_hashes = set()
    for doc in docs:
        clean_text = " ".join(doc.page_content.strip().split())
        content_hash = sha256(clean_text.encode('utf-8')).hexdigest()
        if content_hash not in seen_hashes:
            doc.page_content = clean_text
            unique_docs.append(doc)
            seen_hashes.add(content_hash)

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectordb = Chroma(
        collection_name="amlgo_pdf_chunks",
        embedding_function=embeddings,
        persist_directory="chroma_db"
    )
    vectordb.add_documents(unique_docs)
    vectordb.persist()
    retriever = vectordb.as_retriever()

    llm = Ollama(model="mistral")

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

    query = st.text_input(" Ask your question from the document:")
    if query:
        with st.spinner(" Searching for the most accurate answer..."):
            result = qa_chain.invoke({"query": query})

            st.markdown(" Answer")
            st.info(result['result'])

            st.markdown("---")
            st.markdown("####  Source Chunks (Top 2 Relevant)")
            seen_sources = set()
            filtered_sources = []
            for doc in result['source_documents']:
                content = doc.page_content.strip()
                if not any(content in s for s in seen_sources):
                    seen_sources.add(content)
                    filtered_sources.append(doc)
            for i, doc in enumerate(filtered_sources[:2]):
                st.markdown(f"**Chunk {i+1}:**\n{doc.page_content}")

    st.sidebar.markdown("---")
    st.sidebar.markdown("** Model Used:** `mistral (via Ollama)`")
    st.sidebar.markdown(f"** Chunks Generated:** `{len(unique_docs)}`")
    if st.sidebar.button(" Start Over"):
        st.experimental_rerun()

else:
    st.info(" Please upload a PDF document to begin.")
