# tests/test_integration.py
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_end_to_end_recommendation_flow():
    # 1. Create user
    register_response = client.post("/register", json={
        "email": "test@example.com",
        "password": "test123"
    })
    assert register_response.status_code == 200
    
    # 2. Login
    login_response = client.post("/login", json={
        "email": "test@example.com",
        "password": "test123"
    })
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    # 3. Create profile
    profile_response = client.post("/profile", json={
        "risk_tolerance": "medium",
        "annual_income": 75000,
        "savings": 25000,
        "retirement_horizon_years": 30,
        "goal": "retirement"
    }, headers=headers)
    assert profile_response.status_code == 200
    
    # 4. Get advice
    advice_response = client.post("/advice", headers=headers)
    assert advice_response.status_code == 200
    assert "confidence" in advice_response.json()
    assert advice_response.json()["confidence"] > 0
    
    # 5. Verify recommendation was saved
    recs_response = client.get("/recommendations", headers=headers)
    assert recs_response.status_code == 200
    assert len(recs_response.json()) >= 1