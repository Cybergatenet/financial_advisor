import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import {
  Container,
  Paper,
  Typography,
  TextField,
  Button,
  FormControl,
  InputLabel,
  Select,
  MenuItem,
  Grid,
  Box,
  Alert,
  CircularProgress,
  Stepper,
  Step,
  StepLabel
} from '@mui/material';
import { createProfile, getProfile } from './api';

const steps = ['Risk & Goals', 'Financial Details', 'Review'];

function ProfileSetup() {
  const navigate = useNavigate();
  const [activeStep, setActiveStep] = useState(0);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [existingProfile, setExistingProfile] = useState(null);
  
  const [formData, setFormData] = useState({
    risk_tolerance: 'medium',
    annual_income: '',
    savings: '',
    retirement_horizon_years: '',
    goal: 'retirement'
  });

  // Check if profile already exists
  useEffect(() => {
    const checkProfile = async () => {
      try {
        const res = await getProfile();
        if (res.data) {
          setExistingProfile(res.data);
          // Pre-fill form with existing data
          setFormData({
            risk_tolerance: res.data.risk_tolerance,
            annual_income: res.data.annual_income,
            savings: res.data.savings,
            retirement_horizon_years: res.data.retirement_horizon_years,
            goal: res.data.goal
          });
        }
      } catch (err) {
        // Profile doesn't exist – that's fine
        if (err.response && err.response.status !== 404) {
          console.error(err);
        }
      }
    };
    checkProfile();
  }, []);

  const handleChange = (field) => (event) => {
    setFormData({ ...formData, [field]: event.target.value });
    setError('');
  };

  const validateStep = () => {
    if (activeStep === 0) {
      if (!formData.risk_tolerance) {
        setError('Please select risk tolerance');
        return false;
      }
      if (!formData.goal) {
        setError('Please select financial goal');
        return false;
      }
    }
    if (activeStep === 1) {
      if (!formData.annual_income || parseFloat(formData.annual_income) <= 0) {
        setError('Please enter a valid annual income');
        return false;
      }
      if (!formData.savings || parseFloat(formData.savings) < 0) {
        setError('Please enter valid savings amount');
        return false;
      }
      if (!formData.retirement_horizon_years || parseInt(formData.retirement_horizon_years) < 0) {
        setError('Please enter valid retirement horizon');
        return false;
      }
    }
    return true;
  };

  const handleNext = () => {
    if (validateStep()) {
      setActiveStep((prev) => prev + 1);
    }
  };

  const handleBack = () => {
    setActiveStep((prev) => prev - 1);
    setError('');
  };

  const handleSubmit = async () => {
    if (!validateStep()) return;
    
    setLoading(true);
    setError('');
    
    const payload = {
      risk_tolerance: formData.risk_tolerance,
      annual_income: parseFloat(formData.annual_income),
      savings: parseFloat(formData.savings),
      retirement_horizon_years: parseInt(formData.retirement_horizon_years),
      goal: formData.goal
    };
    
    try {
      await createProfile(payload);
      navigate('/'); // Go to dashboard
    } catch (err) {
      if (err.response && err.response.status === 400) {
        setError('Profile already exists. Redirecting to dashboard...');
        setTimeout(() => navigate('/'), 2000);
      } else {
        setError('Failed to save profile. Please try again.');
      }
      console.error(err);
    }
    setLoading(false);
  };

  if (existingProfile) {
    return (
      <Container maxWidth="md" sx={{ mt: 8 }}>
        <Paper sx={{ p: 4, textAlign: 'center' }}>
          <Typography variant="h5" gutterBottom>
            Profile Already Exists
          </Typography>
          <Typography variant="body1" sx={{ mb: 3 }}>
            Your financial profile is already set up. You can update it here or go to dashboard.
          </Typography>
          <Button variant="contained" onClick={() => navigate('/')}>
            Go to Dashboard
          </Button>
        </Paper>
      </Container>
    );
  }

  return (
    <Container maxWidth="md" sx={{ mt: 4, mb: 4 }}>
      <Paper sx={{ p: 4 }}>
        <Typography variant="h4" gutterBottom align="center">
          Set Up Your Financial Profile
        </Typography>
        <Typography variant="body2" color="textSecondary" align="center" sx={{ mb: 4 }}>
          This helps our AI provide personalized recommendations
        </Typography>
        
        <Stepper activeStep={activeStep} sx={{ mb: 4 }}>
          {steps.map((label) => (
            <Step key={label}>
              <StepLabel>{label}</StepLabel>
            </Step>
          ))}
        </Stepper>
        
        {error && (
          <Alert severity="error" sx={{ mb: 2 }}>
            {error}
          </Alert>
        )}
        
        {activeStep === 0 && (
          <Box>
            <Grid container spacing={3}>
              <Grid item xs={12}>
                <FormControl fullWidth>
                  <InputLabel>Risk Tolerance</InputLabel>
                  <Select
                    value={formData.risk_tolerance}
                    label="Risk Tolerance"
                    onChange={handleChange('risk_tolerance')}
                  >
                    <MenuItem value="low">Low – Prefer safety, minimal losses</MenuItem>
                    <MenuItem value="medium">Medium – Balanced growth and safety</MenuItem>
                    <MenuItem value="high">High – Aggressive growth, accept volatility</MenuItem>
                  </Select>
                </FormControl>
              </Grid>
              <Grid item xs={12}>
                <FormControl fullWidth>
                  <InputLabel>Primary Financial Goal</InputLabel>
                  <Select
                    value={formData.goal}
                    label="Primary Financial Goal"
                    onChange={handleChange('goal')}
                  >
                    <MenuItem value="retirement">Retirement Planning</MenuItem>
                    <MenuItem value="house">Home Purchase</MenuItem>
                    <MenuItem value="education">Education / College Fund</MenuItem>
                    <MenuItem value="wealth">Wealth Accumulation</MenuItem>
                  </Select>
                </FormControl>
              </Grid>
            </Grid>
          </Box>
        )}
        
        {activeStep === 1 && (
          <Box>
            <Grid container spacing={3}>
              <Grid item xs={12}>
                <TextField
                  fullWidth
                  label="Annual Income ($)"
                  type="number"
                  value={formData.annual_income}
                  onChange={handleChange('annual_income')}
                  required
                  InputProps={{ inputProps: { min: 0, step: 1000 } }}
                  helperText="Your gross annual income before taxes"
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  fullWidth
                  label="Total Savings / Liquid Assets ($)"
                  type="number"
                  value={formData.savings}
                  onChange={handleChange('savings')}
                  required
                  InputProps={{ inputProps: { min: 0, step: 1000 } }}
                  helperText="Emergency fund, cash, and liquid investments"
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  fullWidth
                  label="Years Until Retirement"
                  type="number"
                  value={formData.retirement_horizon_years}
                  onChange={handleChange('retirement_horizon_years')}
                  required
                  InputProps={{ inputProps: { min: 0, max: 60 } }}
                  helperText="How many years until you plan to retire?"
                />
              </Grid>
            </Grid>
          </Box>
        )}
        
        {activeStep === 2 && (
          <Box>
            <Typography variant="h6" gutterBottom>Review Your Profile</Typography>
            <Paper variant="outlined" sx={{ p: 2, bgcolor: '#f9f9f9' }}>
              <Grid container spacing={2}>
                <Grid item xs={6}>
                  <Typography variant="body2" color="textSecondary">Risk Tolerance:</Typography>
                </Grid>
                <Grid item xs={6}>
                  <Typography variant="body2">{formData.risk_tolerance}</Typography>
                </Grid>
                <Grid item xs={6}>
                  <Typography variant="body2" color="textSecondary">Annual Income:</Typography>
                </Grid>
                <Grid item xs={6}>
                  <Typography variant="body2">${parseFloat(formData.annual_income || 0).toLocaleString()}</Typography>
                </Grid>
                <Grid item xs={6}>
                  <Typography variant="body2" color="textSecondary">Savings:</Typography>
                </Grid>
                <Grid item xs={6}>
                  <Typography variant="body2">${parseFloat(formData.savings || 0).toLocaleString()}</Typography>
                </Grid>
                <Grid item xs={6}>
                  <Typography variant="body2" color="textSecondary">Retirement Horizon:</Typography>
                </Grid>
                <Grid item xs={6}>
                  <Typography variant="body2">{formData.retirement_horizon_years} years</Typography>
                </Grid>
                <Grid item xs={6}>
                  <Typography variant="body2" color="textSecondary">Goal:</Typography>
                </Grid>
                <Grid item xs={6}>
                  <Typography variant="body2">{formData.goal}</Typography>
                </Grid>
              </Grid>
            </Paper>
            <Typography variant="body2" color="textSecondary" sx={{ mt: 2 }}>
              Click "Submit" to complete your profile and access personalized AI financial advice.
            </Typography>
          </Box>
        )}
        
        <Box sx={{ display: 'flex', justifyContent: 'space-between', mt: 4 }}>
          <Button
            disabled={activeStep === 0}
            onClick={handleBack}
          >
            Back
          </Button>
          {activeStep === steps.length - 1 ? (
            <Button
              variant="contained"
              onClick={handleSubmit}
              disabled={loading}
            >
              {loading ? <CircularProgress size={24} /> : "Submit Profile"}
            </Button>
          ) : (
            <Button
              variant="contained"
              onClick={handleNext}
            >
              Next
            </Button>
          )}
        </Box>
      </Paper>
    </Container>
  );
}

export default ProfileSetup;