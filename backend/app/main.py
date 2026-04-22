from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from . import database, schemas, crud, auth, inference, chat
from .database import SessionLocal

app = FastAPI(title="AI Financial Advisor", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register", response_model=schemas.UserCreate)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db, user)

@app.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    authenticated_user = auth.authenticate_user(db, user.email, user.password)
    if not authenticated_user:
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    access_token = auth.create_access_token(data={"sub": authenticated_user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/profile", response_model=schemas.UserProfileOut)
def create_profile(profile: schemas.UserProfileCreate, db: Session = Depends(get_db), current_user = Depends(auth.get_current_user)):
    existing = crud.get_user_profile(db, current_user.id)
    if existing:
        raise HTTPException(status_code=400, detail="Profile already exists")
    return crud.create_user_profile(db, current_user.id, profile)

@app.get("/profile", response_model=schemas.UserProfileOut)
def get_profile(db: Session = Depends(get_db), current_user = Depends(auth.get_current_user)):
    profile = crud.get_user_profile(db, current_user.id)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile

@app.get("/recommendations", response_model=list[schemas.RecommendationOut])
def get_recommendations(db: Session = Depends(get_db), current_user = Depends(auth.get_current_user)):
    return crud.get_recommendations(db, current_user.id)

@app.post("/advice")
def get_advice(db: Session = Depends(get_db), current_user = Depends(auth.get_current_user)):
    advice_text, confidence = inference.get_recommendation(current_user.id, db)
    return {"advice": advice_text, "confidence": confidence}

@app.post("/chat", response_model=schemas.ChatResponse)
def chat_endpoint(request: schemas.ChatRequest, current_user = Depends(auth.get_current_user)):
    response = chat.process_chat_message(request.message)
    return response

@app.get("/health")
def health():
    return {"status": "ok"}