from fastapi import FastAPI
from app.routes import  health,files
from app.auth import auth_routes
from app.db.database import Base, engine

app = FastAPI()
app.include_router(health.router)
app.include_router(auth_routes.router)

app.include_router(files.router)

Base.metadata.create_all(bind=engine)
@app.get("/")
def root():
    return {"message": "Welcome to the HomeCloud 🚀"}
