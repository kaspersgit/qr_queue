from flask import Flask, request, jsonify, make_response, render_template
from queue_manager import QueueManager
from qr_code_generator import QRCodeGenerator
import hashlib

app = Flask(__name__)
queue_manager = QueueManager()
qr_code_generator = QRCodeGenerator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']

    resp = make_response(render_template('readcookie.html'))
    resp.set_cookie('userID', user)

    return resp

@app.route('/getcookie', methods=['GET'])
def getcookie():
    return request.cookies.get('userID')

@app.route('/usermenu', methods=['GET'])
def usermenu():
    resp = make_response(render_template('usermenu.html'))
    return resp

@app.route('/scan', methods=['GET'])
def scan():
    # user_agent = request.headers.get('User-Agent')
    # ip_address = request.remote_addr
    # identifier = request.cookies.get('userID')
    identifier = request.args.get('userid')

    # identifier = hashlib.sha256(f"{user_agent}{ip_address}{cookies}".encode()).hexdigest()

    if identifier:
        position = queue_manager.get_position(identifier)

        if position is not None:
            queue_manager.remove_from_queue(identifier)
            return jsonify({'message': 'You got removed from the queue.'}), 200
        else:
            queue_manager.add_to_queue(identifier)
            position = queue_manager.get_position(identifier)
            return jsonify({'message': f'You are added to the queue on spot {position}', 'ID': f'{identifier}'}), 200
    return jsonify({'message': 'Invalid request.'}), 400

@app.route('/queue', methods=['GET'])
def get_queue():
    return jsonify({'queue': queue_manager.get_queue()}), 200

@app.route('/position', methods=['GET'])
def get_position():
    user_agent = request.headers.get('User-Agent')
    ip_address = request.remote_addr
    # identifier = request.cookies.get('userID')
    identifier = request.args.get('userid')

    if identifier:
        position = queue_manager.get_position(identifier)
        if position is not None:
            return jsonify({'position': position, 'expected_time_left': f'{position * 2} minutes'}), 200
        return jsonify({f"message': 'Following user is not found in the queue: {identifier}"}), 404
    return jsonify({'message': 'Invalid request.'}), 400

def remove_first_phone():
    queue_manager.remove_from_queue()

if __name__ == '__main__':
    app.run(host="0.0.0.0")

