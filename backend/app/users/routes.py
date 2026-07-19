from fastapi import APIRouter, Depends, status #, HTTPException, status

from app.auth.dependencies import  require_role
from app.database.session import get_db #, Base
from app.users import service as users_service
from app.users.schemas import UserCreate, UserResponse, UserUpdate, UserRoleUpdate
from app.users.constants import UserRole


router=APIRouter(
    prefix="/users",
    tags=["Users"]
)


#Register User
@router.post(
    "/register",
    response_model=UserResponse
)    
def register_user(
    user_data: UserCreate,
    db: Session = Depends(get_db),
    current_user=Depends(require_role([UserRole.OWNER, UserRole.ADMIN]))
):
    return users_service.register_user(user_data, current_user, db)


#List Users
@router.get(
    "/",
    response_model=list[UserResponse]
)    
def get_users(
    skip: int = 0,
    limit: int = 20,
    db: Session = Depends(get_db),
    current_user=Depends(require_role([UserRole.OWNER, UserRole.ADMIN]))
):
    return users_service.get_users(skip, limit, current_user, db)


#Get one user
@router.get(
    "/{user_id}",
    response_model=UserResponse    
)    
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(require_role([UserRole.OWNER, UserRole.ADMIN]))
):
    return users_service.get_user(user_id,current_user, db)


#Update user
@router.put(
    "/{user_id}",
    response_model=UserResponse    
)    
def update_user(
    user_id: int,
    user_data: UserUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(require_role([UserRole.OWNER, UserRole.ADMIN]))
):
    return users_service.update_user(user_id, user_data, current_user, db)

#Delete user
@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role([UserRole.OWNER]))
):
    users_service.delete_user(user_id, current_user, db)


#Deactivate user
@router.patch(
    "/{user_id}/deactivate",
    response_model=UserResponse
)
def deactivate_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role([UserRole.OWNER, UserRole.ADMIN]))
):
    return users_service.deactivate_user(user_id, current_user, db)

#Activate user
@router.patch(
    "/{user_id}/activate",
    response_model=UserResponse
)
def activate_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role([UserRole.OWNER, UserRole.ADMIN]))
):
    return users_service.activate_user(user_id, current_user, db)


@router.patch(
    "/{user_id}/role",
    response_model=UserResponse
)
def update_user_role(
    user_id: int,
    role_update: UserRoleUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role([UserRole.OWNER])
    )
):

    return users_service.update_user_role(user_id,role_update.role, current_user, db)