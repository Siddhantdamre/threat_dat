import React, { useEffect, useState } from "react";
import { fetchThreats } from "../api";

const Dashboard = () => {
  const [threats, setThreats] = useState([]);

  useEffect(() => {
    const loadThreats = async () => {
      const data = await fetchThreats();
      setThreats(data);
    };
    loadThreats();
  }, []);

  return (
    <div className="dashboard">
      <h1>Threat Dashboard</h1>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Message</th>
            <th>Timestamp</th>
          </tr>
        </thead>
        <tbody>
          {threats.map((threat, index) => (
            <tr key={index}>
              <td>{index + 1}</td>
              <td>{threat}</td>
              <td>{new Date().toLocaleString()}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Dashboard;
