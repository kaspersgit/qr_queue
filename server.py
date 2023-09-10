from flask import Flask, request, jsonify, make_response, render_template
from queue_manager import QueueManager
from qr_code_generator import QRCodeGenerator
import hashlib


app = Flask(__name__)

queue_manager = QueueManager()
qr_code_generator = QRCodeGenerator()

# Get simplified assigned name from userid
def getAssignedName(userid):
    if len(userid) < 1:
        aname = 'ShortBoy'
    elif len(userid) < 2:
        aname = 'FlightKid'
    elif len(userid) < 3:
        aname = 'SumoCar'
    elif len(userid) < 4:
        aname = 'BoatStop'
    elif len(userid) < 5:
        aname = 'TrafficMan'
    elif len(userid) < 6:
        aname = 'PunchGirl'
    else:
        aname = 'BossType'

    return aname

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        userid = request.form['nm']
        username = getAssignedName(str(userid))


    resp = make_response(render_template('readcookie.html', userid=userid, username=username))
    resp.set_cookie('userID', userid)
    resp.set_cookie('userName', username)

    return resp

@app.route('/getcookie', methods=['GET'])
def getcookie():
    return [request.cookies.get('userID'), request.cookies.get('userName')]

@app.route('/usermenu', methods=['GET'])
def usermenu():
    identifier = request.cookies.get('userName')

    if identifier:
        position = queue_manager.get_position(identifier)
    else:
        position = None
    resp = make_response(render_template('usermenu.html', position=position, identifier=identifier))
    return resp

@app.route('/scan', methods=['GET'])
def scan():
    # user_agent = request.headers.get('User-Agent')
    # ip_address = request.remote_addr
    # identifier = request.cookies.get('userID')
    identifier = request.args.get('userid')

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
    userid = request.values.get('userid')

    if userid:
        position = queue_manager.get_position(userid) + 1

    if position is not None:
        resp = make_response(render_template('queue_position.html', userid=userid, position=position, timeleft=(position - 1) * 2))
        return resp
    return jsonify({f"message": "Following user is not found in the queue: boom"}), 200


def remove_first_phone():
    queue_manager.remove_from_queue()

if __name__ == '__main__':
    app.run(port=5000, debug=True)

