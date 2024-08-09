import streamlit as st
import subprocess
import os

st.title("DJVU to PDF Converter")

uploaded_file = st.file_uploader("Choose a DJVU file", type="djvu")

if uploaded_file is not None:
    st.write("File details:")
    st.write(f"Filename: {uploaded_file.name}")
    st.write(f"File size: {uploaded_file.size} bytes")

    # Save the uploaded file
    djvu_file_path = os.path.join("temp", uploaded_file.name)
    os.makedirs("temp", exist_ok=True)
    
    with open(djvu_file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"Saved file: {djvu_file_path}")

    # Convert DJVU to PDF
    pdf_file_path = djvu_file_path.replace(".djvu", ".pdf")

    try:
        # Replace 'djvupdf' with your actual conversion command if different
        result = subprocess.run(["djvupdf", djvu_file_path, pdf_file_path], capture_output=True, text=True)
        
        if result.returncode == 0:
            st.success(f"Conversion successful! PDF saved as {pdf_file_path}")
            
            with open(pdf_file_path, "rb") as pdf_file:
                st.download_button(
                    label="Download PDF",
                    data=pdf_file,
                    file_name=os.path.basename(pdf_file_path),
                    mime="application/pdf"
                )
        else:
            st.error(f"Conversion failed: {result.stderr}")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

    # Cleanup
    if os.path.exists(djvu_file_path):
        os.remove(djvu_file_path)
    if os.path.exists(pdf_file_path):
        os.remove(pdf_file_path)


