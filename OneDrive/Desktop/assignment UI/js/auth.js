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