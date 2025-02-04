import React, { useEffect, useState } from 'react';
import { fetchThreats } from './api';

const App = () => {
  const [threats, setThreats] = useState([]);

  useEffect(() => {
    const getThreats = async () => {
      const data = await fetchThreats();
      setThreats(data);
    };
    getThreats();
  }, []);

  return (
    <div className="App">
      <h1>Cybersecurity Threat Detection Platform</h1>
      <h2>Detected Threats</h2>
      <ul>
        {threats.map((threat, index) => (
          <li key={index}>{threat}</li>
        ))}
      </ul>
    </div>
  );
};

export default App;
