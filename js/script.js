// js/script.js
const usernameInput = document.getElementById('username');
const messageInput = document.getElementById('message');
const sendButton = document.getElementById('send');
const chatLog = document.getElementById('chat-log');

sendButton.addEventListener('click', async () => {
  const username = usernameInput.value;
  const message = messageInput.value;

  const response = await fetch('/send', {   // Send request to backend to send message
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, message }),
  });

  const data = await response.json();
  chatLog.innerHTML += `<p>${username}: ${message}</p>`;
  messageInput.value = '';
});
