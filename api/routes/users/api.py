from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.database import db

from . import errors, interface, schemas

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/login", response_model=schemas.LoginResponse)
async def login(data: schemas.LoginUser, db: Session = Depends(db.get_db)):
    try:
        return interface.user_login(
            phone=data.phone, hashed_password=data.hashed_password, db=db
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
