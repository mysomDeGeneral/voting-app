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

@app.post("/admin", response_model=schemas.Admin, tags=["admin"])
async def create_admin(admin: schemas.AdminCreate, db: Session = Depends(get_db)):
    return crud.create_admin(db=db, admin=admin)

@app.get("/admin/{key}", response_model=schemas.Admin, tags=["admin"])
async def get_admin(key: str, db: Session = Depends(get_db)):
    return crud.get_admin(db=db, key=key)

@app.get("/admins", tags=["admin"])
async def get_admins(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_admins(db, skip=skip, limit=limit)

@app.post("/user", response_model=schemas.User, tags=["user"])
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.get("/user/{key}", response_model=schemas.User, tags=["user"])
async def get_user(key: str, db: Session = Depends(get_db)):
    return crud.get_user(db=db, key=key)

@app.get("/users", tags=["user"])
async def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_users(db, skip=skip, limit=limit)

@app.post("/election", response_model=schemas.Election, tags=["election"])
async def create_election(election: schemas.ElectionCreate, db: Session = Depends(get_db)):
    return crud.create_election(db=db, election=election)

@app.get("/election/{key}", response_model=schemas.Election, tags=["election"])
async def get_election(key: int, db: Session = Depends(get_db)):
    return crud.get_election(db=db, key=key)

@app.get("/elections", tags=["election"])
async def get_elections(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_elections(db, skip=skip, limit=limit)

@app.post("/category", response_model=schemas.Category, tags=["category"])
async def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db=db, category=category)

@app.get("/category/{key}", response_model=schemas.Category, tags=["category"])
async def get_category(key: int, db: Session = Depends(get_db)):
    return crud.get_category(db=db, key=key)

@app.get("/categories", tags=["category"])
async def get_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_categories(db, skip=skip, limit=limit)

@app.post("/candidate", response_model=schemas.Candidate, tags=["candidate"])
async def create_candidate(candidate: schemas.CandidateCreate, db: Session = Depends(get_db)):
    return crud.create_candidate(db=db, candidate=candidate)

@app.get("/candidate/{key}", response_model=schemas.Candidate, tags=["candidate"])
async def get_candidate(key: int, db: Session = Depends(get_db)):
    return crud.get_candidate(db=db, key=key)

@app.get("/candidates", tags=["candidate"])
async def get_candidates(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_candidates(db, skip=skip, limit=limit)

@app.post("/vote", response_model=schemas.Vote, tags=["vote"])
async def create_vote(vote: schemas.VoteCreate, db: Session = Depends(get_db)):
    return crud.create_vote(db=db, vote=vote)

@app.get("/vote/{key}", response_model=schemas.Vote, tags=["vote"])
async def get_vote(key: int, db: Session = Depends(get_db)):
    return crud.get_vote(db=db, key=key)

@app.get("/votes", tags=["vote"])
async def get_votes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_votes(db, skip=skip, limit=limit)

@app.post("/vote_detail", response_model=schemas.VoteDetail, tags=["vote_detail"])
async def create_vote_detail(vote_detail: schemas.VoteDetailCreate, db: Session = Depends(get_db)):
    return crud.create_vote_detail(db=db, vote_detail=vote_detail)

@app.get("/vote_detail/{key}", response_model=schemas.VoteDetail, tags=["vote_detail"])
async def get_vote_detail(key: int, db: Session = Depends(get_db)):
    return crud.get_vote_detail(db=db, key=key)

@app.get("/vote_details", tags=["vote_detail"])
async def get_vote_details(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_vote_details(db, skip=skip, limit=limit)






