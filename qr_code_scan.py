import qrcode
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Data structure to store the virtual queue
virtual_queue = []

@app.route('/api/call', methods=['POST'])
def call_api():
    # Access the incoming IP address
    ip_address = request.remote_addr

    # Add the phone to the virtual queue
    virtual_queue.append({'ip_address': ip_address, 'device_id': 'device_id'})

    # Return the position of the phone in the queue
    queue_position = len(virtual_queue)
    response = {'message': 'You have been put in the queue', 'position': queue_position}
    return jsonify(response)

@app.route('/')
def generate_qr_code():
    # Generate the QR code using the current URL (your server's URL + '/api/call')
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(request.host_url + 'api/call')
    qr.make(fit=True)
    qr_img = qr.make_image(fill='black', back_color='white')

    # Save the QR code as an image file
    qr_img.save('static/phone_queue_qr.png')

    return render_template('index.html', queue=virtual_queue)

if __name__ == '__main__':
    app.run()
