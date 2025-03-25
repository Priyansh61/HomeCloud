from fastapi import APIRouter, HTTPException
from .auth_bcrypt import verify_password, get_password_hash
from .auth_handler import sign_jwt
from pydantic import BaseModel


router = APIRouter()

fake_users_db = {}

class User(BaseModel):
    username: str
    password: str

@router.post("/auth/register")
def register(user: User):
    if user.username in fake_users_db:
        raise HTTPException(status_code=400, detail="User already registered")
    fake_users_db[user.username] = get_password_hash(user.password)
    return {"message": "User registered successfully"}

@router.post("/auth/login")
def login(user: User):
    if user.username not in fake_users_db:
        raise HTTPException(status_code=404, detail="User not found")
    if not verify_password(user.password, fake_users_db[user.username]):
        raise HTTPException(status_code=403, detail="Invalid credentials")
    return sign_jwt(user.username)
