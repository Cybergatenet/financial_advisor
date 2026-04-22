import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

# Dummy training – replace with real market data
def train_return_model():
    # Simulate data: features = [P/E, debt/equity, beta, momentum, size]
    np.random.seed(42)
    X = np.random.rand(10000, 5)
    # Target = 0.05 + 0.1*feature0 + noise
    y = 0.05 + 0.1*X[:,0] - 0.02*X[:,1] + 0.03*X[:,2] + np.random.normal(0, 0.01, 10000)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/return_rf.pkl")
    print("Model trained and saved.")

if __name__ == "__main__":
    train_return_model()