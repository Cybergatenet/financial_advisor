import axios from 'axios';

const API = axios.create({ baseURL: 'http://localhost:8000' });

API.interceptors.request.use((req) => {
  const token = localStorage.getItem('token');
  if (token) req.headers.Authorization = `Bearer ${token}`;
  return req;
});

export const register = (data) => API.post('/register', data);
export const login = (data) => API.post('/login', data);
export const createProfile = (data) => API.post('/profile', data);
export const getProfile = () => API.get('/profile');
export const getRecommendations = () => API.get('/recommendations');
export const getAdvice = () => API.post('/advice');
export const sendChat = (message) => API.post('/chat', { message });