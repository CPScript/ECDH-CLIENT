# src/user.py
import os
import pickle

class User:
  def __init__(self, username, public_key, private_key):
    self.username = username
    self.public_key = public_key
    self.private_key = private_key

def create_user(username):
  # Create a new user with a public-private key pair
  public_key, private_key = generate_key_pair()
  user = User(username, public_key, private_key)
  with open(f'{username}.dat', 'wb') as f:
    pickle.dump(user, f)

def get_user(username):
  # Get a user's public-private key pair
  try:
    with open(f'{username}.dat', 'rb') as f:
      user = pickle.load(f)
      return user
  except FileNotFoundError:
    return None
