# src/user.py
import sqlite3

def create_user(username, password):
  conn = sqlite3.connect('users.db')   # Create user in database
  c = conn.cursor()
  c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
  conn.commit()
  conn.close()

def get_user(username):
  conn = sqlite3.connect('users.db')   # Get user from database
  c = conn.cursor()
  c.execute('SELECT * FROM users WHERE username = ?', (username,))
  user = c.fetchone()
  conn.close()
  return user
