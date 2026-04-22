from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime
from .database import RiskTolerance

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserProfileCreate(BaseModel):
    risk_tolerance: RiskTolerance
    annual_income: float
    savings: float
    retirement_horizon_years: int
    goal: str

class UserProfileOut(BaseModel):
    id: int
    user_id: int
    risk_tolerance: RiskTolerance
    annual_income: float
    savings: float
    retirement_horizon_years: int
    goal: str

class RecommendationOut(BaseModel):
    id: int
    advice_text: str
    confidence: float
    explanation: Optional[str] = None
    created_at: datetime

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    reply: str
    intent: str