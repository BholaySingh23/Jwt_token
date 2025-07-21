# main.py
from fastapi import FastAPI, Depends, HTTPException, status, Form
from models import UserLogin, RegisterUser, Token, fake_users_db
from auth import (
    authenticate_user, create_access_token, get_current_user, hash_password
)
from utils import predict, basic_analytics, full_analytics
from fastapi.security import OAuth2PasswordRequestForm

app = FastAPI(title="ML Model API with JWT")

@app.post("/register")
def register_user(user: RegisterUser):
    if user.username in fake_users_db:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    hashed_pwd = hash_password(user.password)
    fake_users_db[user.username] = {
        "username": user.username,
        "hashed_password": hashed_pwd,
        "plan": user.plan.lower()
    }
    return {"message": f"User '{user.username}' registered successfully with plan '{user.plan}'."}

@app.post("/token", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    token = create_access_token(data={"sub": user["username"], "plan": user["plan"]})
    return {"access_token": token, "token_type": "bearer"}

@app.get("/predict")
def get_prediction(user: dict = Depends(get_current_user)):
    return predict({"input": "some input"})

@app.get("/analytics/basic")
def get_basic_analytics(user: dict = Depends(get_current_user)):
    if user["plan"] not in ["premium", "admin"]:
        raise HTTPException(status_code=403, detail="Upgrade to access this feature")
    return basic_analytics()

@app.get("/analytics/full")
def get_full_analytics(user: dict = Depends(get_current_user)):
    if user["plan"] != "admin":
        raise HTTPException(status_code=403, detail="Admins only")
    return full_analytics()
