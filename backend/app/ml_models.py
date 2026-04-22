import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

MODEL_DIR = "models"
os.makedirs(MODEL_DIR, exist_ok=True)

class ReturnPredictor:
    """Random Forest for expected return prediction."""
    def __init__(self):
        self.model = None
        self.load_or_train()

    def load_or_train(self):
        model_path = os.path.join(MODEL_DIR, "return_rf.pkl")
        if os.path.exists(model_path):
            self.model = joblib.load(model_path)
        else:
            # Create a dummy model for demo (in production, train on real data)
            self.model = RandomForestRegressor(n_estimators=10, random_state=42)
            # Dummy training
            X_dummy = np.random.rand(100, 5)
            y_dummy = np.random.rand(100)
            self.model.fit(X_dummy, y_dummy)
            joblib.dump(self.model, model_path)

    def predict(self, features: np.ndarray) -> float:
        """Return expected return (as decimal, e.g., 0.07 for 7%)."""
        if self.model is None:
            return 0.05
        pred = self.model.predict(features.reshape(1, -1))[0]
        return max(0.01, min(0.20, pred))  # Clamp between 1% and 20%

class VolatilityPredictor:
    """Placeholder for LSTM - for demo, returns a simple estimate."""
    def __init__(self):
        pass

    def predict(self, features: np.ndarray) -> float:
        # In real version, load LSTM model and predict
        # For demo: return between 5% and 30%
        return 0.10 + 0.05 * np.random.rand()

class NLU:
    """Placeholder for BERT-based intent classification."""
    def __init__(self):
        pass

    def classify(self, text: str) -> dict:
        """Return intent and entities."""
        text_lower = text.lower()
        if "return" in text_lower or "performance" in text_lower:
            intent = "ask_performance"
        elif "risk" in text_lower:
            intent = "ask_risk"
        elif "buy" in text_lower or "sell" in text_lower:
            intent = "trade_suggestion"
        else:
            intent = "general"
        return {"intent": intent, "entities": {}}

# Global instances
return_predictor = ReturnPredictor()
volatility_predictor = VolatilityPredictor()
nlu = NLU()