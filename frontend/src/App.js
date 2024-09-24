import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [inputText, setInputText] = useState('');
  const [sentiment, setSentiment] = useState('');
  const [error, setError] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const analyzeSentiment = async () => {
    setIsLoading(true);
    setError('');
    try {
      const response = await axios.post('http://localhost:8000/analyze_sentiment', { text: inputText });
      setSentiment(response.data.sentiment_analysis);
    } catch (error) {
      console.error('Error analyzing sentiment:', error);
      console.error('Error response:', error.response);
      setError(error.response?.data?.detail || JSON.stringify(error.response?.data) || error.message || 'An unexpected error occurred. Please try again.');
    }
    setIsLoading(false);
  };

  return (
    <div className="App">
      <h1>Sentiment Analysis</h1>
      <textarea
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
        placeholder="Enter text to analyze"
        rows={5}
        cols={50}
      />
      <br />
      <button onClick={analyzeSentiment} disabled={isLoading}>
        {isLoading ? 'Analyzing...' : 'Analyze Sentiment'}
      </button>
      {sentiment && (
        <div>
          <h2>Sentiment Analysis Result:</h2>
          <p>{sentiment}</p>
        </div>
      )}
      {error && (
        <div style={{color: 'red'}}>
          <h2>Error:</h2>
          <pre>{error}</pre>
        </div>
      )}
    </div>
  );
}

export default App;