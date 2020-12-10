from pydantic import BaseModel

class UserIn(BaseModel):
    username: str
    password: str
    balance: int

class UserOut(BaseModel):
    username: str
    password: str
    balance: int
