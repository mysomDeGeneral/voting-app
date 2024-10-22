from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Welcome to the voting app!"}

@app.post("/admin", response_model=schemas.Admin)
async def create_admin(admin: schemas.AdminCreate, db: Session = Depends(get_db)):
    return crud.create_admin(db=db, admin=admin)

@app.get("/admin/{key}", response_model=schemas.Admin)
async def get_admin(key: str, db: Session = Depends(get_db)):
    return crud.get_admin(db=db, key=key)

@app.post("/user", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.get("/user/{key}", response_model=schemas.User)
async def get_user(key: str, db: Session = Depends(get_db)):
    return crud.get_user(db=db, key=key)