import os, tempfile
import streamlit as st
from utils.uploader import save_uploaded_file
from utils.store import create_vector_store
from utils.authenticate import authenticate

auth  =  authenticate()
if auth[0]:
    openai_api_key = st.session_state.openai_api_key 
    st.subheader('Upload Files')
    uploaded_file = st.file_uploader(
            "Choose .txt,.pdf,.csv,.doc file",
            type=["pdf", "csv", "txt", "doc", "docx"],
            help="You can upload multiple files.",
            accept_multiple_files=False,
        )
    chunk_size = st.number_input(label="Chunk Size(Default 500)", min_value=20, max_value=2000, value=500)
    if st.button("Upload") and uploaded_file:
        save_uploaded_file(uploaded_file)
        create_vector_store(uploaded_file, chunk_size)
