# src/app.py
from flask import Flask, request, jsonify
from crypto import generate_key_pair, ecdh_key_exchange
from user import create_user, get_user
from chat import send_message

app = Flask(__name__)

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
  send_message(user, message)
  return jsonify({'success': True})

if __name__ == '__main__':
  app.run(debug=True)
