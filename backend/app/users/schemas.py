from pydantic import BaseModel, EmailStr



class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    role: str = "employee"
    pay_frequency: str = "weekly"  


class UserUpdate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    role: str  