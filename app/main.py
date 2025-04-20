import streamlit as st
from app.chatbot import build_qa_chain, load_documents, create_vectorstore
import os

st.set_page_config(page_title="Customer Support Bot")
st.title("Customer Support Chatbot")
st.markdown("Ask anything based on our support document")


# create FAISS index on our first run
if not os.path.exists("app/vector_store"):
    docs = load_documents()
    create_vectorstore(docs)

# build QA chain
qa_chain = build_qa_chain()


query = st.text_input("Ask your question:")
if query:
    result = qa_chain(query)
    st.markdown(f"**Answer:** {result['result']}")
    with st.expander("Source Document"):
        for doc in result['source_documents']:
            st.write(doc.page_content[:500])
