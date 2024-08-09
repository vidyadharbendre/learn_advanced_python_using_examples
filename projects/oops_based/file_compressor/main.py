import sys
import os

# # Add the project root directory to PYTHONPATH
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ui.streamlit import run as run_streamlit_ui


def main():
    if len(sys.argv) > 1 and sys.argv[1] == 'cli':
        file_type = input("Enter file type (image/pdf): ").lower()
        input_path = input("Enter input file path: ")
        output_path = input("Enter output file path: ")

        if file_type == 'image':
            from compressor.image_compressor import ImageCompressor
            compressor = ImageCompressor()
        elif file_type == 'pdf':
            from compressor.pdf_compressor import PDFCompressor
            compressor = PDFCompressor()
        else:
            print("Unsupported file type!")
            return

        compressor.compress(input_path, output_path)
    else:
        run_streamlit_ui()

if __name__ == "__main__":
    main()
