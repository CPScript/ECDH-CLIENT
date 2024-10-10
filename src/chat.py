# src/chat.py
import socket
import threading

class Chat:
  def __init__(self, user):
    self.user = user
    self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.socket.bind(('localhost', 8080))
    self.socket.listen(1)

  def send_message(self, message):
    # Send a message to another user
    recipient = get_user(message['recipient'])
    if recipient:
      # Establish a connection with the recipient
      connection = establish_connection(recipient.username, 8080)
      # Send the message
      send_message(connection, message['message'])
      # Close the connection
      connection.close()

  def receive_message(self):
    # Receive a message from another user
    connection, address = self.socket.accept()
    message = receive_message(connection)
    print(f'Received message from {address}: {message}')
    connection.close()

def establish_connection(username, port):
  # Establish a connection with another user
  socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  socket.connect((username, port))
  return socket

def send_message(socket, message):
  # Send a message over a socket
  socket.sendall(message.encode())

def receive_message(socket):
  # Receive a message over a socket
  message = socket.recv(1024).decode()
  return message
