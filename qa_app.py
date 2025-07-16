import os
from pathlib import Path
import streamlit as st
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAI
from langchain.chains import RetrievalQA

# Load the embeddings and Chroma DB
embeddings = OpenAIEmbeddings()
db = Chroma(persist_directory="chroma_db", embedding_function=embeddings)
retriever = db.as_retriever()

# Create the LLM
llm = OpenAI(temperature=0)

# Create the RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True
)

# Streamlit UI
st.set_page_config(page_title="Author Papers Q&A", page_icon="📄")
st.title("📄 Ask Questions About the Author's Papers")

query = st.text_input("Enter your question:")

if query:
    result = qa_chain(query)

    st.subheader("Answer")
    st.write(result["result"])

    st.subheader("Sources")
    for doc in result["source_documents"]:
        st.write(f"- {doc.metadata['source']}")

