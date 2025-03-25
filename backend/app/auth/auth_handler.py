import time
from jose import  jwt
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("JWT_SECRET")
ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")

def sign_jwt(user_id: int) -> dict[str, str]:
    payload = {
        "user_id": user_id,
        "expires": time.time() + 3600
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token}


def decode_jwt(token: str) -> dict[str, str]:
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return decoded if decoded["expires"] >= time.time() else None
    except :
        return {}