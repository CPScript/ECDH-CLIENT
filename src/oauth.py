# src/oauth.py
from flask_oauthlib.client import OAuth2Client

class OAuth:
  def __init__(self, app):
    self.app = app
    self.oauth = OAuth2Client(self.app)

  def authorize(self, username, password):
    auth = self.oauth.authorize(username, password) # Authenticate user using OAuth
    return auth

  def register(self, username, password):
    auth = self.oauth.register(username, password)     # Register user using OAuth
    return auth
