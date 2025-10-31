from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.schemas.auth_schema import RegisterRequest, LoginRequest, TokenResponse
from backend.core.database import get_db, engine
from backend.core.security import get_password_hash, verify_password, create_access_token
from backend.models.hr_model import HR
from sqlalchemy.exc import IntegrityError

router = APIRouter()

@router.post("/register", response_model=dict)
def register(payload: RegisterRequest, db: Session = Depends(get_db)):
    # simple: store HR user in hrs table (for demo)
    hashed = get_password_hash(payload.password)
    hr = HR(name=payload.name, email=payload.email)
    # for demo we cheat and add a password field dynamically; better: separate User model w/ password
    # But to keep minimal — add a simple "users" table later. For now, respond success.
    try:
        # naive raw insert via SQLAlchemy core for demonstration; better: add User model
        db.add(hr)
        db.commit()
        db.refresh(hr)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Email already registered")
    return {"id": hr.id, "name": hr.name, "email": hr.email}

@router.post("/login", response_model=TokenResponse)
def login(payload: LoginRequest):
    # In real implementation: lookup user and verify hashed password.
    # For scaffold: return a token with subject=email (this is placeholder)
    token = create_access_token(subject=payload.email)
    return {"access_token": token}
