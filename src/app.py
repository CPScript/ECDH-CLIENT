# src/app.py
from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
from crypto import generate_key_pair, ecdh_key_exchange
from user import create_user, get_user
from chat import Chat

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/register', methods=['POST'])
def register():
  username = request.json['username']
  create_user(username)
  return jsonify({'success': True})

@app.route('/send', methods=['POST'])
def send_message():
  username = request.json['username']
  message = request.json['message']
  user = get_user(username)
  chat = Chat(user)
  chat.send_message(message)
  return jsonify({'success': True})

@socketio.on('connect')
def connect():
  print('Client connected')

@socketio.on('disconnect')
def disconnect():
  print('Client disconnected')

@socketio.on('message')
def handle_message(message):
  emit('message', message, broadcast=True)

if __name__ == '__main__':
  socketio.run(app, debug=True)
