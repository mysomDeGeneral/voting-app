from pydantic import BaseModel
from typing import List, Optional
from datetime import date, datetime

class AdminBase(BaseModel):
    username: str
    email: str

class AdminCreate(AdminBase):
    password: str

class AdminUpdate(AdminBase):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

class Admin(AdminBase):
    id: int

    class ConfigDict:
        from_attributes = True

class UserBase(BaseModel):
    username: str
    email: str
    full_name: str
    date_of_birth: date

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: Optional[str] = None


class User(UserBase):
    id: int
    is_verified: bool

    class ConfigDict:
        from_attributes = True

class ElectionBase(BaseModel):
    title: str
    description: str
    start_date: datetime
    end_date: datetime

class ElectionCreate(ElectionBase):
    pass

class ElectionUpdate(ElectionBase):
    is_active: Optional[bool] = None

class Election(ElectionBase):
    id: int
    is_active: bool

    class ConfigDict:
        from_attributes = True

class CategoryBase(BaseModel):
    name: str
    description: str
    election_id: int

class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int

    class ConfigDict:
        from_attributes = True

class CandidateBase(BaseModel):
    user_id: int
    description: str
    category_id: int

class CandidateCreate(CandidateBase):
    pass

class Candidate(CandidateBase):
    id: int

    class ConfigDict:
        from_attributes = True

class VoteBase(BaseModel):
    user_id: int
    election_id: int
    timestamp: datetime

class VoteCreate(VoteBase):
    pass

class Vote(VoteBase):
    id: int

    class ConfigDict:
        from_attributes = True

class VoteDetailBase(BaseModel):
    vote_id: int
    category_id: int
    candidate_id: int

class VoteDetailCreate(VoteDetailBase):
    pass

class VoteDetail(VoteDetailBase):
    id: int

    class ConfigDict:
        from_attributes = True
