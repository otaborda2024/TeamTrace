from pydantic import BaseModel, EmailStr


class EmployeeCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str


class EmployeeUpdate(BaseModel):
    full_name: str
    email: EmailStr
    role: str    

class JobSiteCreate(BaseModel):
    name: str
    latitude: Float
    longitude: Float
    radius_meters: Float

