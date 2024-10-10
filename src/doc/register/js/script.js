// script.js
const usernameInput = document.getElementById('username');
const passwordInput = document.getElementById('password');
const confirmPasswordInput = document.getElementById('confirm-password');
const registerButton = document.getElementById('register');

registerButton.addEventListener('click', async () => {
  const username = usernameInput.value;
  const password = passwordInput.value;
  const confirmPassword = confirmPasswordInput.value;

  // Send request to backend to register
  const response = await fetch('/register', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, password, confirmPassword }),
  });

  const data = await response.json();
  if (data.success) {
    // Registration successful, redirect to login page
    window.location.href = '/src/doc/login/index.html';
  } else {
    console.error('Registration failed');
  }
});
