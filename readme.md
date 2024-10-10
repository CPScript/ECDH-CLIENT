## How it works:

* The user accesses the website and is prompted to log in or register.
* The frontend (JavaScript) sends a request to the backend (Python) to create a new user or authenticate an existing user.
* The backend (Python) handles user creation or authentication and generates a public-private key pair using the Haskell cryptography library.
* The backend (Python) establishes a connection with the client using the C networking library.
* The client (JavaScript) sends a message to the backend (Python), which encrypts the message using the ECDH key exchange and symmetric encryption.
* The backend (Python) sends the encrypted message to the recipient's backend, which decrypts the message using the shared secret key.
* The recipient's backend (Python) sends the decrypted message to the recipient's frontend (JavaScript), which displays the message in the chat interface.
