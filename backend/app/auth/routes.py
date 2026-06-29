from fastapi import APIRouter, Depends #, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm #OAuth2PasswordBearer,
#from sqlalchemy.orm import Session

from app.auth import service as auth_service
from app.auth import dependencies as auth_dependencies
from app.auth import schemas as auth_schemas
from app.database.session import get_db #, Base
from app.users.schemas import UserCreate


#app = FastAPI()

router=APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

# This looks for the token in the request headers
#oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")



@router.post(
    "/register",
    response_model=auth_schemas.UserResponse
)    
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return auth_service.register_user(user, db)


@router.post(   
    "/login",
    response_model=auth_schemas.Token,
    summary="Login user",
    description="Authenticate a user and return a JWT access token."
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    return auth_service.login_user(
        username=form_data.username,
        password=form_data.password,
        db=db
    )


@router.get(    
    "/me",
    response_model=auth_schemas.UserResponse
)
def me(current_user = Depends(auth_dependencies.get_current_user)):
    return current_user
