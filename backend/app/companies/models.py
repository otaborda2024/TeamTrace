from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from app.database.session import Base
from app.database.base_class import TimestampMixin


class Company(Base,TimestampMixin):
    __tablename__ = "companies"
    
    id = Column(Integer, primary_key=True, index=True)    
    name = Column(String, nullable=False )
    is_active = Column(Boolean, default=True)   
    users = relationship("User", back_populates="company")