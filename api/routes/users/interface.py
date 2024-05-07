from sqlalchemy.orm import Session
from . import models, schemas, errors
from api.utils.auth import auth_bearer


def create_user(phone: str, hashed_password: str, db: Session):
    phone = "+91" + phone if len(phone) == 10 else phone
    user = get_user(phone=phone, hashed_password=hashed_password, db=db)
    if user:
        return user
    user = models.Users(phone=phone, hashed_password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user(phone: str, hashed_password: str, db: Session):
    phone = "+91" + phone if len(phone) == 10 else phone
    user = (
        db.query(models.Users)
        .filter(
            models.Users.phone == phone, models.Users.hashed_password == hashed_password
        )
        .scalar()
    )
    return user


def user_login(phone: str, hashed_password: str, db: Session):
    user = create_user(phone=phone, hashed_password=hashed_password, db=db)
    db.add(user)
    db.commit()
    db.refresh(user)
    data = {
        "id": user.id,
        "phone": user.phone,
    }
    access_token = auth_bearer.create_access_token(data=data)
    return {"access_token": access_token, "user": user}
