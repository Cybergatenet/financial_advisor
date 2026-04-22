from sqlalchemy.orm import Session
from . import database, schemas
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user_by_email(db: Session, email: str):
    return db.query(database.User).filter(database.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed = pwd_context.hash(user.password)
    db_user = database.User(email=user.email, hashed_password=hashed)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_user_profile(db: Session, user_id: int, profile: schemas.UserProfileCreate):
    db_profile = database.UserProfile(user_id=user_id, **profile.dict())
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile

def get_user_profile(db: Session, user_id: int):
    return db.query(database.UserProfile).filter(database.UserProfile.user_id == user_id).first()

def save_recommendation(db: Session, user_id: int, advice_text: str, confidence: float, rule_id: int = None):
    rec = database.Recommendation(user_id=user_id, advice_text=advice_text, confidence=confidence, rule_id=rule_id)
    db.add(rec)
    db.commit()
    db.refresh(rec)
    return rec

def get_recommendations(db: Session, user_id: int, limit: int = 10):
    return db.query(database.Recommendation).filter(database.Recommendation.user_id == user_id).order_by(database.Recommendation.created_at.desc()).limit(limit).all()