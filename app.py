import qrcode
from flask import Flask, request, render_template
import socket
from utils.queues import * 

app = Flask(__name__)

@app.route('/api/call', methods=['POST'])
def call_api():
    # Extract unique details from the request, such as phone number, device ID, or any other relevant information
    phone_number = request.form.get('phone_number')
    device_id = request.form.get('device_id')

    # Place the phone into the virtual queue using the unique details
    # Call your API or perform any other necessary operations here

    return 'Phone added to the virtual queue'

@app.route('/')
def generate_qr_code():
    # Get the IP address of the machine running the Flask server
    ip_address = socket.gethostbyname(socket.gethostname())
    base_url = f'http://{ip_address}:5000'

    # Generate the QR code using the dynamic IP address
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(base_url + '/api/call')
    qr.make(fit=True)
    qr_img = qr.make_image(fill='black', back_color='white')

    # Save the QR code as an image file
    qr_img.save('static/phone_queue_qr.png')

    return render_template('index.html')

if __name__ == '__main__':
    app.run()
