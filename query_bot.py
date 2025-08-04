from dotenv import load_dotenv
import os

load_dotenv() 

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import HuggingFaceHub
from langchain.chains import RetrievalQA

embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

vectordb = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embedding_model
)

llm = HuggingFaceHub(
    repo_id="google/flan-t5-small",
    task="text2text-generation",
    model_kwargs={"temperature": 0.3, "max_new_tokens": 512}
)

qa = RetrievalQA.from_chain_type(llm=llm, retriever=vectordb.as_retriever())

while True:
    query = input("\n Ask something about your document (or type 'exit'): ")
    if query.lower() in ["exit", "quit"]:
        break
    result = qa.invoke(query)
    print("\n Answer:", result['result'])  

    print("\n Answer:", result)
