# src/app.py
from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
from flask_oauthlib.client import OAuth2Client
from crypto import generate_key_pair, ecdh_key_exchange
from user import create_user, get_user
from chat import Chat
from rabbitmq import RabbitMQ
from oauth import OAuth

app = Flask(__name__)
socketio = SocketIO(app)
oauth = OAuth(app)

# OAuth configuration
oauth.config['client_id'] = 'your_client_id'
oauth.config['client_secret'] = 'your_client_secret'
oauth.config['authorization_url'] = 'https://example.com/authorize'
oauth.config['token_url'] = 'https://example.com/token'

@app.route('/login', methods=['POST'])
def login():
  username = request.json['username']
  password = request.json['password']

  auth = oauth.authorize(username, password) # Authenticate user using OAuth
  if auth:
    socketio.emit('connect', {'username': username}) # Login successful, establish WebSocket connection
    return jsonify({'success': True})
  else:
    return jsonify({'success': False})

@app.route('/register', methods=['POST'])
def register():
  username = request.json['username']
  password = request.json['password']

  auth = oauth.register(username, password) # Register user using OAuth
  if auth:
    return jsonify({'success': True}) # Registration successful
  else:
    return jsonify({'success': False})

@app.route('/send', methods=['POST'])
def send_message():
  username = request.json['username']
  message = request.json['message']

  rabbitmq = RabbitMQ() # Send message using RabbitMQ
  rabbitmq.send_message(username, message)
  return jsonify({'success': True})

@ socketio.on('connect')
def connect(username): # Establish WebSocket connection
  chat = Chat(username)
  chat.join_room()

@socketio.on('disconnect')
def disconnect(): # Disconnect WebSocket connection
  chat.leave_room()

if __name__ == '__main__':
  socketio.run(app, host='0.0.0.0', port=8080)
