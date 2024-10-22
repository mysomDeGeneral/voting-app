from sqlalchemy.orm import Session
from . import models, schemas

def get_admin(db: Session, key: str):
    return db.query(models.Admin).filter(models.Admin.username == key).first()

def get_admins(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Admin).offset(skip).limit(limit).all()

def create_admin(db: Session, admin: schemas.AdminCreate):
    db_admin = models.Admin(**admin.model_dump())
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    return db_admin


def get_user(db: Session, key: str):
    return db.query(models.User).filter(models.User.username == key).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_election(db: Session, key: int):
    return db.query(models.Election).filter(models.Election.id == key).first()

def get_elections(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Election).offset(skip).limit(limit).all()

def create_election(db: Session, election: schemas.ElectionCreate):
    db_election = models.Election(**election.model_dump())
    db.add(db_election)
    db.commit()
    db.refresh(db_election)
    return db_election

def get_category(db: Session, key: int):
    return db.query(models.Category).filter(models.Category.id == key).first()

def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Category).offset(skip).limit(limit).all()

def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(**category.model_dump())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_candidate(db: Session, key: int):
    return db.query(models.Candidate).filter(models.Candidate.id == key).first()

def get_candidates(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Candidate).offset(skip).limit(limit).all()

def create_candidate(db: Session, candidate: schemas.CandidateCreate):
    db_candidate = models.Candidate(**candidate.model_dump())
    db.add(db_candidate)
    db.commit()
    db.refresh(db_candidate)
    return db_candidate

def get_vote(db: Session, key: int):
    return db.query(models.Vote).filter(models.Vote.id == key).first()

def get_votes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Vote).offset(skip).limit(limit).all()

def create_vote(db: Session, vote: schemas.VoteCreate):
    db_vote = models.Vote(**vote.model_dump())
    db.add(db_vote)
    db.commit()
    db.refresh(db_vote)
    return db_vote

def get_vote_detail(db: Session, key: int):
    return db.query(models.VoteDetail).filter(models.VoteDetail.id == key).first()

def get_vote_details(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.VoteDetail).offset(skip).limit(limit).all()

def create_vote_detail(db: Session, vote_detail: schemas.VoteDetailCreate):
    db_vote_detail = models.VoteDetail(**vote_detail.model_dump())
    db.add(db_vote_detail)
    db.commit()
    db.refresh(db_vote_detail)
    return db_vote_detail





