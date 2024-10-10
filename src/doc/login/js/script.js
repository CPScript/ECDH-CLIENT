// src/doc/login/js/script.js
const usernameInput = document.getElementById('username');
const passwordInput = document.getElementById('password');
const loginButton = document.getElementById('login');
const chatLog = document.getElementById('chat-log');

loginButton.addEventListener('click', async () => {
  const username = usernameInput.value;
  const password = passwordInput.value;

  // Send request to backend to login
  const response = await fetch('/login', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, password }),
  });

  const data = await response.json();
  if (data.success) {
    // Login successful, establish WebSocket connection
    const socket = new WebSocket('ws://localhost:8080');
    socket.onmessage = (event) => {
      const message = event.data;
      chatLog.innerHTML += `<p>${message}</p>`;
    };
  } else {
    console.error('Login failed');
  }
});
