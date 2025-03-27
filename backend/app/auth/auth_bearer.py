
from fastapi import APIRouter, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.auth.auth_handler import decode_jwt
from fastapi import Request

class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request : Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid or expired token")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code")

    def verify_jwt(self, jwt_token: str):
        payload = decode_jwt(jwt_token)
        return payload is not None