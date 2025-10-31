from fastapi import FastAPI
from backend.core.config import settings
from backend.routers import auth_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="HireBOT Backend", version="0.1.0")

# CORS - fine-tune origins in production
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router.router, prefix="/api/auth", tags=["auth"])


@app.get("/")
def read_root():
    return {"status": "ok", "service": "HireBOT Backend"}
