// js/script.js
const usernameInput = document.getElementById('username');
const messageInput = document.getElementById('message');
const sendButton = document.getElementById('send');
const chatLog = document.getElementById('chat-log');

sendButton.addEventListener('click', async () => {
  const username = usernameInput.value;
  const message = messageInput.value;

  // Send request to backend to send message
  const response = await fetch('/send', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, message }),
  });

  const data = await response.json();
  chatLog.innerHTML += `<p>${username}: ${message}</p>`;
  messageInput.value = '';
});

// Add event listener for receiving messages
socket.onmessage = (event) => {
  const message = event.data;
  chatLog.innerHTML += `<p>${message}</p>`;
};

// Establish a connection with the backend
const socket = new WebSocket('ws://localhost:8080');

// Send a request to the backend to register the user
fetch('/register', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ username: usernameInput.value }),
});
