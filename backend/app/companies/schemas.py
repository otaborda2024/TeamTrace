from pydantic import BaseModel

class CompanyCreate(BaseModel):
    id: int 
    name: str
    active: bool=True
    created_at: datetime
  