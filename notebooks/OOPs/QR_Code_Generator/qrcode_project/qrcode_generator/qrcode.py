import qrcode

class QRCodeGenerator:
    def __init__(self, url, filename="qrcode.png"):
        self.url = url
        self.filename = filename

    def generate_qr_code(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(self.url)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        img.save(self.filename)
        print(f"QR Code saved as {self.filename}")
