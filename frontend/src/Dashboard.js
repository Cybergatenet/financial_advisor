import React, { useState, useEffect } from 'react';
import { Container, Paper, Typography, Button, List, ListItem, ListItemText, CircularProgress, Box } from '@mui/material';
import { getRecommendations, getAdvice, getProfile } from './api';

function Dashboard() {
  const [recommendations, setRecommendations] = useState([]);
  const [loading, setLoading] = useState(false);
  const [profile, setProfile] = useState(null);

  useEffect(() => {
    fetchProfile();
    fetchRecommendations();
  }, []);

  const fetchProfile = async () => {
    try {
      const res = await getProfile();
      setProfile(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  const fetchRecommendations = async () => {
    try {
      const res = await getRecommendations();
      setRecommendations(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  const requestNewAdvice = async () => {
    setLoading(true);
    try {
      await getAdvice();
      fetchRecommendations();
    } catch (err) {
      console.error(err);
    }
    setLoading(false);
  };

  return (
    <Container maxWidth="md" sx={{ mt: 4 }}>
      <Paper sx={{ p: 3 }}>
        <Typography variant="h4" gutterBottom>Financial Advisor Dashboard</Typography>
        {profile && (
          <Box mb={2}>
            <Typography variant="body1">Risk Tolerance: {profile.risk_tolerance}</Typography>
            <Typography variant="body1">Annual Income: ${profile.annual_income.toLocaleString()}</Typography>
            <Typography variant="body1">Savings: ${profile.savings.toLocaleString()}</Typography>
          </Box>
        )}
        <Button variant="contained" onClick={requestNewAdvice} disabled={loading} sx={{ mb: 3 }}>
          {loading ? <CircularProgress size={24} /> : "Get New Advice"}
        </Button>
        <Typography variant="h5">Past Recommendations</Typography>
        <List>
          {recommendations.map((rec) => (
            <ListItem key={rec.id} divider>
              <ListItemText primary={rec.advice_text} secondary={`Confidence: ${(rec.confidence*100).toFixed(0)}% | ${new Date(rec.created_at).toLocaleString()}`} />
            </ListItem>
          ))}
          {recommendations.length === 0 && <Typography>No recommendations yet. Click "Get New Advice".</Typography>}
        </List>
      </Paper>
    </Container>
  );
}

export default Dashboard;