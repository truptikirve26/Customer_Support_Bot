# Customer Support Chatbot with LangChain (RAG-based)

This project showcases a Retrieval Augmented Generation (RAG) chatbot built using [LangChain](https://www.langchain.com/), [OpenAI](https://platform.openai.com/), and [Streamlit](https://streamlit.io/). It allows users or customer service agents to interact conversationally with internal support documentation (e.g., refund policies) to quickly surface relevant answers.

Inspired by a real world usecase I worked on, this version uses synthetic documents to demonstrate architecture and capabilities while preserving confidentiality.

## Features

- **Document aware Q&A** over internal policies
- **RAG pipeline** using LangChain, OpenAIEmbeddings, FAISS 
- **COnversational Interface** using Streamlit
- Easy API managemnet with .env support
Extendable to use multiple pdfs, feedback data or databases

## Tech Stack
- **LangChain**: LLMchaining and Retrieval
- **OpenAI**: LLM and embeddings
- **FAISS**: - vector store for document retrieval
- **Streamlit** - Frontend chatbot interface
- **Pypdf** - document loading
- **dotenv** - Environment variable management



# how to Run
Install dependencies
pip install -r requirements.txt


Add your OPENAI API key

Create a .env file in your root directory
OPENAI_API_KEY = xxxx-xx-xxx


Add a PDF to data/ directory
Use the sample refund_policy.pdf or use your own


Run the app
streamlit run app/main.py


The project is a simplified, anonymized version of a support assistant that I helped build in a prodcution environment. 
The architecture closely reflects what we used internally:
- FAQ retrieval based on real support tickets
- Policy based document responses
- Language model orchestration with LangChain


All data in the repository are synthetic and for demo purpose only

