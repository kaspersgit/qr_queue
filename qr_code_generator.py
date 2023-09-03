import qrcode

class QRCodeGenerator:
    def generate_qr_code(self, data: str, file_path: str) -> None:
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill="black", back_color="white")
        img.save(file_path)

if __name__ == '__main__':
    ab = QRCodeGenerator()
    ab.generate_qr_code('http://192.168.50.91:5000/scan', 'qr_scan.png')
    ab.generate_qr_code('http://192.168.50.91:5000/position', 'qr_position.png')
