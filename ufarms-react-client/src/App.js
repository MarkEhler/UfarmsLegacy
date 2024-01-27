import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

// creating an env variable for local or cloud deployments would look like
// const apiUrl = process.env.NODE_ENV === 'prod'
//   ? 'https://your-heroku-app-name.herokuapp.com'
//   : 'http://localhost:8000';

function App() {
  const [currentTime, setCurrentTime] = useState(0);

// Use apiUrl in your fetch calls
// fetch(`${apiUrl}/time`)
  useEffect(() => {
    fetch('/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
    });
  }, []);

  return (
    <div className="App">
      <header className="App-header">

        ... no changes in this part ...

        <p>The current time is {currentTime}.</p>
      </header>
    </div>
  );
}

export default App;