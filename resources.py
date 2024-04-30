import streamlit as st
import os

def list_pdf_files():
    pdf_files = [file for file in os.listdir("pdf_files") if file.endswith(".pdf")]
    return pdf_files

def app():
    st.title("Resources")
    pdf_files = list_pdf_files()

    for pdf_file in pdf_files:
        st.markdown(f"### {pdf_file}")
        download_button = st.download_button(
            label=f"Download {pdf_file}",
            data=open(f"pdf_files/{pdf_file}", "rb").read(),
            file_name=pdf_file
        )
