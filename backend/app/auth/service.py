from fastapi import HTTPException
#from sqlalchemy.orm import Session

from app.users.models import User
from app.users.constants import UserRole
from app.companies.models import Company

#from app.auth.schemas import UserCreate
from app.core import security
#from app.core.security import get_password_hash


#Register a company and its owner
def register_company(data, db: Session):

    existing_user = (
        db.query(User)
        .filter(User.email == data.email)
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    company = Company(
        name=data.company_name
    )

    db.add(company)

    # Flush sends the INSERT to the database so the company gets its id,
    # but it does NOT commit the transaction yet.
    db.flush()

    user = User(
        first_name=data.first_name,
        last_name=data.last_name,
        email=data.email,
        password_hash=security.get_password_hash(data.password),
        role=UserRole.OWNER,
        company_id=company.id
    )

    db.add(user)

    db.commit()

    db.refresh(company)
    db.refresh(user)

    return {
        "message": "Company created successfully.",
        "company_id": company.id,
        "owner_id": user.id
    }


#User login
def login_user(username: str, password: str, db: Session):
    user = (
        db.query(User)
        .filter(User.email == username)
        .first()
    )

    if not user or not security.verify_password(password, user.password_hash):
        raise HTTPException(
            status_code=401,
            detail="Incorrect email or password"
        )

    if user.is_active == False:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Deactivated user"
    )

    access_token = security.create_access_token(
        data={
            "sub": str(user.id),
            "role": user.role,
            "company_id": user.company_id
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


