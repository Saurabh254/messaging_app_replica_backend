from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.database import db

router = APIRouter(prefix="/users", tags=["users"])


@router.get("")
async def get_all_users(db: Session = Depends(db.get_db)):
    return {"list": [db]}
