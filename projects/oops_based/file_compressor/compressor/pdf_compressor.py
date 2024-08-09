# compressor/pdf_compressor.py
import subprocess
from .base_compressor import BaseCompressor

class PDFCompressor(BaseCompressor):

    def __init__(self, pdf_settings='/screen'):
        self.pdf_settings = pdf_settings

    def compress(self, input_path, output_path):
        gs_command = [
            'gs',
            '-sDEVICE=pdfwrite',
            '-dCompatibilityLevel=1.4',
            f'-dPDFSETTINGS={self.pdf_settings}',
            '-dNOPAUSE',
            '-dBATCH',
            '-sOutputFile=' + output_path,
            input_path
        ]
        subprocess.run(gs_command, check=True)
        print(f"PDF saved at: {output_path}")
