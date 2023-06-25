import streamlit as st
from utils.authenticate import authenticate

# Initialize session state variables
if 'openai_api_key' not in st.session_state:
	st.session_state.openai_api_key = ""
        
st.set_page_config(page_title="Fusion AI - Home", page_icon="🦜️🔗")

auth  =  authenticate()

if auth[0]:
    auth[1].logout('Logout', 'main', key='unique_key')
    st.header("Welcome to Fusion AI - Experiments! 👋")
    st.markdown(
        """
        This experiment uses **Retrieval Augmented Generation (RAG)** to retrieve data from outside a foundation model and augment your prompts by adding the relevant retrieved data in context.
        
        **👈 Provide the API keys in Settings, and select a upload documents from the sidebar to get started.**

        ##### Upload Documents
        * Supports Multiple File Upload.
        * Supported Formats - pdf, txt, doc, docx, csv.
        * Uses chromaDB as Vector Store.
        * *Note: Set Chunk size for the uploaded document. This impact the semantic similarity result.*

        ##### Chat with your Documents
        * Conversation chain and In memory for chat based outputs.
        * Pass Context from Uploaded documents.
        * Select type of retrieval from vector db. This includes **stuff**, **map-reduce** etc. [Document](https://python.langchain.com/docs/modules/chains/document/)
        * Enable Prompt Engineering.

        ##### Document Summary
        * Summarizing documents using LangChain and Chroma.
        * References: [Blog](https://alphasec.io/summarize-documents-with-langchain-and-chroma) | [Source Code](https://github.com/alphasecio/langchain-examples/blob/main/chroma-summary) | [Python Notebook](https://github.com/alphasecio/langchain-examples/blob/main/chroma-summary/langchain_doc_summarizer.ipynb)
        
        ### Upcoming Usecases

        1. REST API as Context Provider
        2. Oracle Database as Context Provider
        3. Combine multiple context for example - Oracle + PDF + JSON
        """
    )
