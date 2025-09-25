import React, { useState } from 'react';
import Login from './pages/Login';
import Signup from './pages/Signup';
import Comments from './pages/Comments';
import MovieInfo from './pages/MovieInfo';
import Layout from './components/Layout';

function App() {
  const [page, setPage] = useState('login');
  const [currentUser, setCurrentUser] = useState(null);

  const [flashMessages] = useState([]);

  const handleNavigate = (targetPage) => {
    setPage(targetPage);
  };

  const handleLoginSuccess = (user) => {
    setCurrentUser(user);
    setPage('home');
  };

  const handleLogout = () => {
    setCurrentUser(null);
    setPage('login');
  };

  let content;
  if (page === 'login') {
    content = <Login onNavigate={handleNavigate} onLoginSuccess={handleLoginSuccess} />;
  } else if (page === 'signup') {
    content = <Signup onNavigate={handleNavigate} onSignupSuccess={handleLoginSuccess} />;
  } else if (page === 'home') {
    content = (
      <div>
        <MovieInfo />
        <Comments onNavigate={handleNavigate} />
      </div>
    );
  }

  return (
    <Layout currentUser={currentUser} flashMessages={flashMessages} onLogout={handleLogout}>
      {content}
    </Layout>
  );
}

export default App;
