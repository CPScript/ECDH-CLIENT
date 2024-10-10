// js/script.js
const usernameInput = document.getElementById('username');
const passwordInput = document.getElementById('password');
const loginButton = document.getElementById('login');
const registerButton = document.getElementById('register');
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

registerButton.addEventListener('click', async () => {
  const username = usernameInput.value;
  const password = passwordInput.value;

  // Send request to backend to register
  const response = await fetch('/register', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, password }),
  });

  const data = await response.json();
  if (data.success) {
    console.log('Registration successful');
  } else {
    console.error('Registration failed');
  }
});
