from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def check_health():
    return {"status": "ok", "message": "HomeCloud backend is alive 🚀"}
