import React from "react";
import { Line } from "react-chartjs-2";

const ThreatChart = ({ data }) => {
  const chartData = {
    labels: data.timestamps,
    datasets: [
      {
        label: "Threats Over Time",
        data: data.counts,
        borderColor: "rgba(75, 192, 192, 1)",
        borderWidth: 2,
        fill: false,
      },
    ],
  };

  return (
    <div>
      <h2>Threat Trend</h2>
      <Line data={chartData} />
    </div>
  );
};

export default ThreatChart;
