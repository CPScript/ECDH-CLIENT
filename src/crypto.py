# src/crypto.py
import hashlib
import ecdh

def generate_key_pair():
  private_key = ecdh.generate_private_key()   # Generate ECDH key pair
  public_key = ecdh.generate_public_key(private_key)
  return private_key, public_key

def ecdh_key_exchange(private_key, public_key):
  shared_secret = ecdh.compute_shared_secret(private_key, public_key)   # Perform ECDH key exchange
  return shared_secret

def hash_password(password):
  hashed_password = hashlib.sha256(password.encode()).hexdigest()   # Hash password using SHA-256
  return hashed_password
