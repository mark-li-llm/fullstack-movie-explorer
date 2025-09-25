import React, { useEffect, useState } from 'react';
import PropTypes from 'prop-types';

function Comments({ onNavigate }) {
  const [comments, setComments] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchData() {
      try {
        const res = await fetch('http://localhost:8080/api/comments', {
          credentials: 'include',
        });
        const data = await res.json();
        if (res.ok) {
          setComments(data.comments || []);
        } else {
          alert(data.error || 'Failed to fetch comments');
        }
      } catch (err) {
        alert('Network error');
      }
      setLoading(false);
    }
    fetchData();
  }, []);

  const handleDelete = (id) => {
    setComments((prev) => prev.filter((item) => item.id !== id));
  };

  const handleChangeRating = (id, newRating) => {
    setComments((prev) =>
      prev.map((item) =>
        item.id === id ? { ...item, rating: Number(newRating) } : item,
      ),
    );
  };

  const handleChangeComment = (id, newComment) => {
    setComments((prev) =>
      prev.map((item) =>
        item.id === id ? { ...item, comment: newComment } : item,
      ),
    );
  };

  const handleAdd = () => {
    const newItem = {
      id: Date.now(),
      movie_id: 999,
      rating: 3,
      comment: '',
    };
    setComments((prev) => [...prev, newItem]);
  };

  const handleSave = async () => {
    try {
      const res = await fetch('http://localhost:8080/api/comments', {
        method: 'POST',
        credentials: 'include',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ comments }),
      });
      const data = await res.json();
      if (res.ok) {
        alert(data.message || 'Comments saved');
      } else {
        alert(data.error || 'Failed to save');
      }
    } catch (err) {
      alert('Network error');
    }
  };

  if (loading) {
    return <div>Loading comments...</div>;
  }

  return (
    <div>
      <h2>My Comments</h2>
      <button type="button" onClick={handleAdd}>
        + Add Comment
      </button>
      <hr />
      {comments.map((item) => (
        <div
          key={item.id}
          style={{
            border: '1px solid grey',
            margin: '8px',
            padding: '8px',
          }}
        >
          <p>
            Movie ID:
            {item.movie_id}
          </p>
          <label htmlFor={`rating-${item.id}`}>
            Rating:
            <input
              id={`rating-${item.id}`}
              type="number"
              min="1"
              max="5"
              value={item.rating}
              onChange={(e) => handleChangeRating(item.id, e.target.value)}
            />
          </label>
          <br />
          <label htmlFor={`comment-${item.id}`}>
            Comment:
            <textarea
              id={`comment-${item.id}`}
              value={item.comment}
              onChange={(e) => handleChangeComment(item.id, e.target.value)}
            />
          </label>
          <br />
          <button type="button" onClick={() => handleDelete(item.id)}>
            Delete
          </button>
        </div>
      ))}
      <hr />
      <button type="button" onClick={handleSave}>
        Save
      </button>
      <br />
      <br />
      <button type="button" onClick={() => onNavigate('login')}>
        Logout / Go to Login
      </button>
    </div>
  );
}

Comments.propTypes = {
  onNavigate: PropTypes.func.isRequired,
};

export default Comments;
