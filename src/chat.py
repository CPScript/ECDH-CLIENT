# src/chat.py
import socketio

class Chat:
  def __init__(self, username):
    self.username = username
    self.room = 'chat'

  def join_room(self):
    socketio.join_room(self.room) # Join chat room

  def leave_room(self):
    socketio.leave_room(self.room) # Leave chat room

  def send_message(self, message):
    socketio.emit('message', {'username': self.username, 'message': message}, room=self.room) # Send message to chat room
