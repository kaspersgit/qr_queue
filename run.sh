# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install Flask
pip install flask

# Install qrcode
pip install qrcode

# Activate the virtual environment
source venv/bin/activate

# Start the server
python server.py

# Add a phone to the queue
curl -X POST -H "Content-Type: application/json" -d '{"phone_id": "153"}' http://localhost:5000/scan

# Get the current queue
curl http://localhost:5000/queue

# Get the position of a phone in the queue
curl http://localhost:5000/position?phone_id=123
