from pydantic import BaseModel, EmailStr

class Token(BaseModel):
    access_token: str
    token_type: str

class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str


class Message(BaseModel):
    message: str

class CompanyRegister(BaseModel):
    company_name: str
    first_name: str
    last_name: str
    email: EmailStr
    password: str