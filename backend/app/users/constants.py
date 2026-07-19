from enum import Enum


class UserRole(str, Enum):
    EMPLOYEE = "employee"    
    ADMIN = "admin"
    OWNER = "owner"
