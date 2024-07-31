#python -m unittest discover -s tests -p "tes*.py"

import os
import unittest
from qrcode_generator.qrcode import QRCodeGenerator

class TestQRCodeGenerator(unittest.TestCase):
    def test_generate_qr_code(self):
        url = "https://www.example.com"
        filename = "test_qrcode.png"
        qr_generator = QRCodeGenerator(url, filename)
        qr_generator.generate_qr_code()
        # Check if file is created
        self.assertTrue(os.path.exists(filename))
        # Clean up
        os.remove(filename)

if __name__ == "__main__":
    unittest.main()
