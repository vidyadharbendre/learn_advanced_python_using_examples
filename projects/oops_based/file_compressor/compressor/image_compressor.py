# compressor/image_compressor.py
from PIL import Image
from .base_compressor.py import BaseCompressor

class ImageCompressor(BaseCompressor):

    def __init__(self, max_size=800):
        self.max_size = max_size

    def compress(self, input_path, output_path):
        image = Image.open(input_path)
        image.thumbnail((self.max_size, self.max_size))
        image.save(output_path, quality=85, optimize=True)
        print(f"Image saved at: {output_path}")
