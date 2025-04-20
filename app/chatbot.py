import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_community.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def load_documents():
    loader = PyPDFLoader("data/refund_policy.pdf")
    documents = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    return splitter.split_documents(documents)

def create_vectorstore(docs):
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local("app/vector_store")
    return vectorstore

def load_vectorstore():
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    return FAISS.load_local("app/vector_store", embeddings)

def build_qa_chain():
    llm = OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)
    vs = load_vectorstore()
    return RetrievalQA.from_chain_type(llm=llm, retriever=vs.as_retriever(), return_source_documents=True)


