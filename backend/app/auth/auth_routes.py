from fastapi import APIRouter, HTTPException, Depends
from app.auth.auth_bcrypt import verify_password, get_password_hash
from app.auth.auth_handler import sign_jwt
from pydantic import BaseModel

from app.db.database import get_db
from app.models.user import User
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserLogin, UserOut

from app.utils.hash import hash_password

router = APIRouter()

@router.post("/auth/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    hashed_pw = hash_password(user.password)
    new_user = User(email=user.email, password=hashed_pw)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user  # auto-converted to UserOut

@router.post("/auth/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = sign_jwt(db_user.id)

    return {"access_token": token}
