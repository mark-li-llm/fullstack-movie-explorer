import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

function MovieInfo({ onNavigate }) {
  const [movie, setMovie] = useState(null);
  const [loading, setLoading] = useState(true);
  const [rating, setRating] = useState('');
  const [comment, setComment] = useState('');
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('http://localhost:8080/api/random_movie', {
      credentials: 'include',
    })
      .then((res) => res.json())
      .then((data) => {
        if (data.error) {
          setError(data.error);
        } else {
          setMovie(data);
        }
        setLoading(false);
      })
      .catch((err) => {
        console.error('Failed to fetch movie data:', err);
        setError('Failed to fetch movie data.');
        setLoading(false);
      });
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch('http://localhost:8080/api/rate_comment', {
      method: 'POST',
      credentials: 'include',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        movie_id: movie.movie_id,
        rating,
        comment,
      }),
    })
      .then((res) => res.json())
      .then((data) => {
        console.log('Review submitted:', data);
        return fetch('http://localhost:8080/api/random_movie', {
          credentials: 'include',
        });
      })
      .then((res) => res.json())
      .then((updatedMovie) => {
        setMovie(updatedMovie);
        setRating('');
        setComment('');
      })
      .catch((err) => {
        console.error('Failed to submit review:', err);
        setError('Failed to submit review.');
      });
  };

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return (
      <div>
        <span>Error:</span>
        <span>{error}</span>
      </div>
    );
  }

  return (
    <div>
      <h2>{movie.title}</h2>
      {movie.poster_url && (
        <img
          src={movie.poster_url}
          alt="Movie Poster"
          style={{ maxWidth: '300px' }}
        />
      )}
      <p>{movie.tagline}</p>
      <p>Genres:</p>
      <p>{movie.genres && movie.genres.join(', ')}</p>
      {movie.wiki_url && (
        <p>
          <a
            href={movie.wiki_url}
            target="_blank"
            rel="noopener noreferrer"
          >
            More Info on Wikipedia
          </a>
        </p>
      )}
      <h3>Reviews:</h3>
      {movie.reviews && movie.reviews.length > 0 ? (
        <ul>
          {movie.reviews.map((review) => (
            <li key={review.id}>
              <div>
                <span>{review.rating}</span>
              </div>
              <div>
                <span>-</span>
              </div>
              <div>
                <span>{review.comment}</span>
              </div>
            </li>
          ))}
        </ul>
      ) : (
        <p>No reviews yet.</p>
      )}
      <h3>Submit Your Review</h3>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="rating">
            Rating:
            <input
              id="rating"
              type="number"
              value={rating}
              onChange={(e) => setRating(e.target.value)}
              required
            />
          </label>
        </div>
        <div>
          <label htmlFor="comment">
            Comment:
            <input
              id="comment"
              type="text"
              value={comment}
              onChange={(e) => setComment(e.target.value)}
              required
            />
          </label>
        </div>
        <button type="submit">Submit Review</button>
      </form>
      <button
        type="button"
        onClick={() => onNavigate && onNavigate('comments')}
      >
        Go to Comments Page
      </button>
    </div>
  );
}

MovieInfo.propTypes = {
  onNavigate: PropTypes.func,
};

MovieInfo.defaultProps = {
  onNavigate: () => {},
};

export default MovieInfo;
