# ui/streamlit_ui.py
import streamlit as st
from compressor.image_compressor import ImageCompressor
from compressor.pdf_compressor import PDFCompressor

def run():
    st.title("File Compressor")

    file_type = st.selectbox("Select file type", ['Image', 'PDF'])
    uploaded_file = st.file_uploader(f"Upload a {file_type}", type=['jpg', 'jpeg', 'png', 'pdf'])
    max_size = st.slider("Select maximum size (only for images)", 100, 2000, 800)

    if st.button("Compress"):
        if uploaded_file is not None:
            input_path = f"temp_{uploaded_file.name}"
            with open(input_path, 'wb') as f:
                f.write(uploaded_file.getbuffer())

            output_path = f"compressed_{uploaded_file.name}"

            if file_type == 'Image':
                compressor = ImageCompressor(max_size)
            elif file_type == 'PDF':
                compressor = PDFCompressor()

            compressor.compress(input_path, output_path)

            with open(output_path, 'rb') as f:
                st.download_button(label="Download compressed file", data=f, file_name=output_path, mime=None)

        else:
            st.error("Please upload a file to compress.")
