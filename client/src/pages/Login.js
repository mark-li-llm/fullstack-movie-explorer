import React, { useState } from 'react';
import PropTypes from 'prop-types';

function Login({ onNavigate }) {
  const [username, setUsername] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:8080/api/login', {
        method: 'POST',
        credentials: 'include',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username }),
      });
      const data = await response.json();
      if (response.ok) {
        alert(data.message || 'Login success!');
        onNavigate('comments');
      } else {
        alert(data.error || 'Login failed');
      }
    } catch (err) {
      alert('Network error');
    }
  };

  return (
    <div>
      <h2>Login Page</h2>
      <form onSubmit={handleSubmit}>
        <label htmlFor="username">
          Username:
          <input
            id="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
        </label>
        <br />
        <button type="submit">Login</button>
      </form>
      <br />
      <button type="button" onClick={() => onNavigate('signup')}>
        Go to Signup
      </button>
    </div>
  );
}

Login.propTypes = {
  onNavigate: PropTypes.func.isRequired,
};

export default Login;
