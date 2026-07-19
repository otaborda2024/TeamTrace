from pydantic import BaseModel, EmailStr
from app.users.constants import UserRole

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
     

class UserRoleUpdate(BaseModel):
    role: UserRole


class UserUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    email: EmailStr | None = None


class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    role: UserRole
    company_id: int
    is_active: bool

    class Config:
        from_attributes = True


#class UserResponse(BaseModel):
#    id: int
#    first_name: str
 #   last_name: str
 #   email: str


        #company_id: int 
        #  pay_frequency: str = "weekly"
    #        role: str = "employee"
   # active: bool=True