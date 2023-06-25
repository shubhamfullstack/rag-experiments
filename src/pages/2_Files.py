import streamlit as st
import os
from utils.authenticate import authenticate

def show_files():
    files = os.listdir("data")
    st.write("Uploaded Files:")
    for file in files:
        st.write("📁 " + file)

auth  =  authenticate()
if auth[0]:
    show_files()
    
