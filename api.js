import axios from 'axios';

const API_URL = 'http://localhost:5000/api/detect';

export const fetchThreats = async () => {
  try {
    const response = await axios.get(API_URL);
    return response.data.threats;
  } catch (error) {
    console.error('Error fetching threats:', error);
    return [];
  }
};
