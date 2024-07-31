from qrcode_generator.qrcode import QRCodeGenerator

def main():
    url = input("Enter the URL for the QR code: ")
    filename = input("Enter the filename for the QR code (with .png extension): ")
    qr_generator = QRCodeGenerator(url, filename)
    qr_generator.generate_qr_code()

if __name__ == "__main__":
    main()
