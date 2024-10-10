// src/doc/register/js/script.js
const usernameInput = document.getElementById('username');
const passwordInput = document.getElementById('password');
const registerButton = document.getElementById('register');


registerButton.addEventListener('click', async () => {
  const username = usernameInput.value;
  const password = passwordInput.value;

  const response = await fetch('/register', { // Send request to backend to register
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
