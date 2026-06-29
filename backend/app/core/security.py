import datetime
from jose import jwt
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

# 1. Setup Password Hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 2. Secret keys (In production, move these to a hidden .env file!)
SECRET_KEY = "SUPER_SECRET_TEAM_TRACE_KEY_DO_NOT_SHARE"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
MAX_PASSWORD_LENGTH = 72


# This looks for the token in the request headers
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# Function to turn a plain password into a secure hash
def get_password_hash(password: str) -> str:
    if len(password.encode("utf-8")) > MAX_PASSWORD_LENGTH:
        raise ValueError("Password too long (max 72 bytes*)")
    return pwd_context.hash(password)
   # return password
   # return pwd_context.hash(password)

# Function to verify if a typed password matches the saved hash
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# Function to generate the signed digital ticket (JWT)
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    #print(expire)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    #return expire
    return encoded_jwt

def decode_access_token(token: str):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        return payload
    except JWTError:
        return None 


 