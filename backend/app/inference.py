import numpy as np
from . import rule_engine, ml_models
from .database import SessionLocal, get_user_profile
from .crud import save_recommendation

def get_recommendation(user_id: int, db_session):
    # Retrieve user profile
    profile_obj = get_user_profile(db_session, user_id)
    if not profile_obj:
        return "Please complete your financial profile first."
    profile = {
        "risk_tolerance": profile_obj.risk_tolerance.value,
        "annual_income": profile_obj.annual_income,
        "savings": profile_obj.savings,
        "retirement_horizon_years": profile_obj.retirement_horizon_years,
        "goal": profile_obj.goal
    }
    # Rule engine evaluation
    engine = rule_engine.RuleEngine()
    # For age, we would need a user age field; using a placeholder
    user_age = 40  # In real system, compute from user's birthdate
    actions = engine.evaluate(profile, user_age)
    rule_advice = engine.get_recommendation_text(actions)

    # ML predictions (for a sample security, e.g., SPY)
    # In production, iterate over candidate securities
    dummy_features = np.array([profile['annual_income']/100000, profile['savings']/100000, 
                               profile['retirement_horizon_years'], 1.0, 0.05])  # example features
    expected_return = ml_models.return_predictor.predict(dummy_features)
    volatility = ml_models.volatility_predictor.predict(dummy_features)
    sharpe = expected_return / volatility if volatility > 0 else 0

    ml_advice = f"Based on market data, the model suggests an expected return of {expected_return:.1%} with volatility {volatility:.1%}. Sharpe ratio: {sharpe:.2f}."

    # Combine rule and ML advice
    full_advice = f"{rule_advice}\n\n{ml_advice}"
    confidence = 0.7 + 0.2 * (sharpe / 1.0) if sharpe < 1.0 else 0.9
    confidence = min(0.95, confidence)

    # Save recommendation to database
    save_recommendation(db_session, user_id, full_advice, confidence)

    return full_advice, confidence