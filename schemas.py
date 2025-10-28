from pydantic import BaseModel
class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True

        from pydantic import BaseModel

# ========================
# Student Schemas
# ========================
# schemas.py
from pydantic import BaseModel

class StudentBase(BaseModel):
    name: str
    age: int
    grade: str

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int

    class Config:
        from_attributes = True  # replaces orm_mode in v2



# ========================
# User Schemas
# ========================
class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True

