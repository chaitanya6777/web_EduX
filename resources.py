# resources.py

import streamlit as st
import os

# Function to list all PDF files in the directory
def list_pdf_files():
    pdf_files = [file for file in os.listdir("pdf_files") if file.endswith(".pdf")]
    return pdf_files

# Define app for Resources section
def app():
    st.title("Resources")

    # List all PDF files in the directory
    pdf_files = list_pdf_files()

    # Display PDF files in Resources section
    for pdf_file in pdf_files:
        st.markdown(f"### {pdf_file}")
        download_button = st.download_button(
            label=f"Download {pdf_file}",
            data=open(f"pdf_files/{pdf_file}", "rb").read(),
            file_name=pdf_file
        )
