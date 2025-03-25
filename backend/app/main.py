from fastapi import FastAPI
from .routes import  health
from .auth import auth_routes
app = FastAPI()
app.include_router(health.router)
app.include_router(auth_routes.router)

@app.get("/")
def root():
    return {"message": "Welcome to HomeCloud 🚀"}
