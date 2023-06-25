import streamlit as st
import os

def save_uploaded_file(uploaded_file):
    st.spinner(text="In progress...")
    with open(os.path.join("data", uploaded_file.name), "wb") as file:
        file.write(uploaded_file.getbuffer())
    st.success("Files uploaded successfully!")