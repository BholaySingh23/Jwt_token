# models.py
from pydantic import BaseModel

# Dummy user db
fake_users_db = {
    "bholay": {
        "username": "bholay",
        "hashed_password": "$2b$12$Q0eNzglyx0nIKF0D3aZqDu5rwfNBEuKJDAVvHzOXhHDLByrFJ7hhy",  # 'test123'
        "plan": "admin"
    },
    "alice": {
        "username": "alice",
        "hashed_password": "$2b$12$M9CqQOT0NlCWuFQyKTNqhuWmEihf8FJtvVjUBjVYdJXixpKn1nKJW",  # 'adminpass'
        "plan": "free"
    }
}

class Token(BaseModel):
    access_token: str
    token_type: str

class UserLogin(BaseModel):
    username: str
    password: str

class RegisterUser(BaseModel):
    username: str
    password: str
    plan: str  # free, premium, or admin
