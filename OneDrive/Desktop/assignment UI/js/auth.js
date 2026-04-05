const USERS = {
  'admin': { password: 'admin123', role: 'admin' },
  'attendant': { password: 'park2026', role: 'attendant' }
};

function login(username, password) {
  const user = USERS[username];
  if (user && user.password === password) {
    localStorage.setItem('parkease_user', JSON.stringify(user));
    if (user.role === 'admin') {
      window.location.href = 'reports.html';
    } else {
      window.location.href = 'dashboard.html';
    }
  } else {
    document.getElementById('login-error').textContent = 'Invalid username or password';
  }
}
document.addEventListener('DOMContentLoaded', function() {
  const form = document.getElementById('login-form');
  if (form) {
    form.addEventListener('submit', function(e) {
      e.preventDefault();
      const username = document.getElementById('username').value.trim();
      const password = document.getElementById('password').value;
      login(username, password);
    });
  }
});