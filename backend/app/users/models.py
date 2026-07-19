from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy import Enum
from sqlalchemy.orm import relationship
from app.database.session import Base
from app.database.base_class import TimestampMixin
from app.users.constants import UserRole


class User(Base,TimestampMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True )
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False )    
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(Enum(UserRole), default=UserRole.EMPLOYEE)
    is_active = Column(Boolean, default=True)
    company = relationship("Company", back_populates="users")
