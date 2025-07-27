from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    password: str
    
class UserCreate(BaseModel):
    name: str
    email: str
    password: str