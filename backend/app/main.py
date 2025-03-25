from fastapi import FastAPI
from .routes import  health

app = FastAPI()
app.include_router(health.router)

@app.get("/")
def root():
    return {"message": "Welcome to HomeCloud 🚀"}
