import React, { useState } from 'react';
import axios from 'axios';

function PredictComponent() {
  const [features, setFeatures] = useState([]);
  const [prediction, setPrediction] = useState('');

  const handleSubmit = async () => {
    try {
      const response = await axios.post('http://localhost:5000/predict', {
        features: features
      });
      setPrediction(response.data.prediction[0]);   // Assuming one prediction
    } catch (error) {
      console.error('Error making prediction:', error);
    }
  };

  return (
    <div>
      <h1>Make Prediction</h1>
      {/* Assume you have inputs to set features */}
      <button onClick={handleSubmit}>Predict</button>
      {prediction && <p>Prediction: {prediction}</p>}
    </div>
  );
}

export default PredictComponent;
