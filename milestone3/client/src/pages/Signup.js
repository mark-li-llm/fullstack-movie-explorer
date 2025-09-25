import React, { useState } from 'react';
import PropTypes from 'prop-types';

function Signup({ onNavigate }) {
  const [username, setUsername] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await fetch('http://localhost:8080/api/signup', {
        method: 'POST',
        credentials: 'include',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username }),
      });
      const data = await res.json();
      if (res.ok) {
        alert(data.message || 'Signup success!');
        onNavigate('login');
      } else {
        alert(data.error || 'Signup failed');
      }
    } catch (err) {
      alert('Network error');
    }
  };

  return (
    <div>
      <h2>Signup Page</h2>
      <form onSubmit={handleSubmit}>
        <label htmlFor="signup-username">
          Username:
          <input
            id="signup-username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
        </label>
        <br />
        <button type="submit">Sign Up</button>
      </form>
      <br />
      <button type="button" onClick={() => onNavigate('login')}>
        Go to Login
      </button>
    </div>
  );
}

Signup.propTypes = {
  onNavigate: PropTypes.func.isRequired,
};

export default Signup;
