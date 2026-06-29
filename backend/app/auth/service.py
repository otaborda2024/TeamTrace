from fastapi import HTTPException
#from sqlalchemy.orm import Session

from app.users.models import User
#from app.auth.schemas import UserCreate
from app.core import security
#from app.core.security import get_password_hash

#Register user
def register_user(
    userInfo: UserCreate,
    db: Session
):
    existing_user = (
        db.query(User)
        .filter(User.email == userInfo.email)
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    hashed_password = security.get_password_hash(
        userInfo.password
    )

    new_user = User(
        first_name=userInfo.first_name,
        last_name=userInfo.last_name,
        email=userInfo.email,
        password_hash=hashed_password,
        role=userInfo.role,
        pay_frequency=userInfo.pay_frequency

    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {
        "id": new_user.id,
        "first_name": new_user.first_name,
        "last_name": new_user.last_name,
        "email": new_user.email
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

    access_token = security.create_access_token(
        data={"sub": user.email}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

