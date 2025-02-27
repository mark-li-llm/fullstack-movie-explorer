import React from 'react';
import PropTypes from 'prop-types';
import './Layout.css';

function Layout({
  currentUser,
  flashMessages,
  children,
  onLogout,
}) {
  return (
    <div className="layout-container">
      <header className="layout-header">
        <h1>Movie Explorer</h1>
        {currentUser ? (
          <p>
            Logged in as:
            <strong>{currentUser.username}</strong>
            {' | '}
            <button type="button" onClick={onLogout}>
              Logout
            </button>
          </p>
        ) : (
          <p>
            <a href="/login">Login</a>
            {' | '}
            <a href="/signup">Sign Up</a>
          </p>
        )}
      </header>
      <div className="container">
        {children}
      </div>
      {flashMessages && flashMessages.length > 0 && (
        <ul className="flash-messages">
          {flashMessages.map((msg, index) => (
            <li key={index}>{msg}</li>
          ))}
        </ul>
      )}
    </div>
  );
}

Layout.propTypes = {
  currentUser: PropTypes.shape({
    username: PropTypes.string.isRequired,
  }),
  flashMessages: PropTypes.arrayOf(PropTypes.string),
  children: PropTypes.node.isRequired,
  onLogout: PropTypes.func.isRequired,
};

Layout.defaultProps = {
  currentUser: null,
  flashMessages: [],
};

export default Layout;
