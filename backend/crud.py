from sqlalchemy.orm import Session
from . import models, schemas

def get_admin(db: Session, key: str):
    return db.query(models.Admin).filter(models.Admin.username == key).first()

def create_admin(db: Session, admin: schemas.AdminCreate):
    db_admin = models.Admin(**admin.model_dump())
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    return db_admin


def get_user(db: Session, key: str):
    return db.query(models.User).filter(models.User.username == key).first()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

