from fastapi import APIRouter, Depends
from api.database import db
from sqlalchemy.orm import Session
from sqlalchemy import text

router = APIRouter(prefix="/users", tags=["users"])


@router.get("")
async def get_all_users(db: Session = Depends(db.get_db)):
    return {"list": [db]}
