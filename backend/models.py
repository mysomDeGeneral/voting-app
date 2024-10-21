from sqlalchemy import String, Integer, Column, Date, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()
class Admin(Base):
    __tablename__ = 'admin'

    id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    full_name = Column(String(255), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    is_verified = Column(Boolean, default=False)

class Election(Base):
    __tablename__ = 'election'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    is_active = Column(Boolean, default=False)

class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    election_id = Column(Integer, ForeignKey('election.id'))

class Candidate(Base):
    __tablename__ = 'candidate'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    description = Column(String(255), nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'))

class Vote(Base):
    __tablename__ = 'vote'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    election_id = Column(Integer, ForeignKey('election.id'))
    timestamp = Column(Date, nullable=False)

class VoteDetail(Base):
    __tablename__ = 'vote_detail'

    id = Column(Integer, primary_key=True)
    vote_id = Column(Integer, ForeignKey('vote.id'))
    category_id = Column(Integer, ForeignKey('category.id'))
    candidate_id = Column(Integer, ForeignKey('candidate.id'))
