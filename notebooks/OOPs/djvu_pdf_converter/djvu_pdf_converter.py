import streamlit as st
import subprocess
import os

def convert_djvu_to_pdf(djvu_file_path, pdf_file_path):
    try:
        subprocess.check_call(['ddjvu', '-format=pdf', djvu_file_path, pdf_file_path])
        return True
    except subprocess.CalledProcessError as e:
        st.error(f'Error during conversion: {e}')
        return False

st.title('DJVU to PDF Converter')

uploaded_file = st.file_uploader("Upload a DJVU file", type="djvu")

if uploaded_file is not None:
    # Save the uploaded file to disk
    djvu_file_path = os.path.join("temp", uploaded_file.name)
    os.makedirs(os.path.dirname(djvu_file_path), exist_ok=True)
    with open(djvu_file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Set the output PDF file path
    pdf_file_path = djvu_file_path.replace('.djvu', '.pdf')

    if st.button("Convert to PDF"):
        if convert_djvu_to_pdf(djvu_file_path, pdf_file_path):
            with open(pdf_file_path, "rb") as f:
                st.download_button("Download PDF", f, file_name=os.path.basename(pdf_file_path))
