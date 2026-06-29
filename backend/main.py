
from fastapi import FastAPI
from app.auth.routes import router as auth_router

#To call create_all in developing fase.

# Import all models so SQLAlchemy registers them and 
from app.database.session import Base, engine
import app.users.models
#import app.jobsites.models
#import app.projects.models

Base.metadata.create_all(bind=engine)

#End of create all in developing fase


app = FastAPI(
    title="TeamTrace API",
    version="0.1.0"
)


app.include_router(auth_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to TeamTrace API"
    }

'''
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import models
import schemas
import security
import database

# Create the database file immediately
models.database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# This looks for the token in the request headers
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


# This allows your React app to talk to your Python app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/register")
def register_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    # Check if email already exists
    existing_user=db.query(models.Employee).filter(models.Employee.email==employee.email).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Secure the password and save
    hashed_password=security.get_password_hash(employee.password)    

    # Create a new employee
    new_employee=models.Employee(full_name=employee.full_name,email=employee.email,password_hash=hashed_password)
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return {"message": "Employee registered succesfully", "employee_id": new_employee.id, "email": new_employee.email, "role": new_employee.role}

@app.get("/employees")
def get_employees(db: Session=Depends(get_db)):
    return db.query(models.Employee).all()


@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    # 1. Look for the employee in the database
    db_employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    
    # 2. If it's not there, tell the user
    if db_employee is None:
        return {"message": "Employee not found"}
        
    # 3. If it is there, delete it and save
    db.delete(db_employee)
    db.commit()
    return {"message": f"Employee {employee_id} deleted successfully"}


@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, employee: schemas.EmployeeUpdate, db: Session = Depends(get_db)):
   
    # 1. Look for the employee in the database
    db_employee = db.query(models.Employee).filter(models.Employee.id == employee.id).first()
    
    # 2. If it's not there, tell the user
    if db_employee is None:
        return {"message": "Employee not found"}
        
    # 3. If it is there, update the fields
    db_employee.name = employee.full_name
    db_employee.email = employee.email
    db_employee.role = employee.role
    
    # 4. Save the changes to the database
    db.commit()
    db.refresh(db_employee)
    return {"message": f"Employee {employee.id} updated successfully"}

'''
'''

    # --- 1. Endpoint to Register a New Employee ---
@app.post("/register")
def register_employee(full_name: str, email: str, password: str, db: Session = Depends(get_db)):

# --- ADD THIS LINE HERE ---
    print(f"DEBUG: Registering {full_name} with password: {password} (Length: {len(password.encode("utf-8"))})")
    # --------------------------


    # Check if email is already taken
    existing_user = db.query(models.Employee).filter(models.Employee.email == email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Secure the password and save
    hashed_pwd = security.get_password_hash(password)
    new_employee = models.Employee(full_name=full_name, email=email, password_hash=hashed_pwd)
    
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return {"message": "Employee registered successfully!", "id": new_employee.id}
'''
'''
# --- 2. Endpoint to Login and get the Token ---
@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # Find the user by email
    user = db.query(models.Employee).filter(models.Employee.email == form_data.username).first()
    
    # Check if user exists and password is correct
    if not user or not security.verify_password(form_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Create and return the token
    access_token = security.create_access_token(data={"sub": user.email})
  #  oauth2_scheme = OAuth2PasswordBearer(access_token=access_token, token_type="bearer")
    return {"access_token": access_token, "token_type": "bearer"}



# --- 3. A Protected Route (Requires Login!) ---
@app.get("/secure-data")
def get_secure_data(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        # 1. Decode and validate the token using your security logic
        payload = security.decode_access_token(token)
        email = payload.get("sub")
        
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token identity")
            
        # 2. Grab the actual employee from the database
        user = db.query(models.Employee).filter(models.Employee.email == email).first()
        if user is None:
            raise HTTPException(status_code=401, detail="User no longer exists")
            
    except Exception:
        raise HTTPException(status_code=401, detail="Token is expired or altered!")

    # 3. If everything is clear, return the secure data tailored to them!
    return {
        "message": f"Congrats {user.full_name}! You accessed secure data.",
        "secret_code": "TeamTrace-2026",
        "logged_in_as": user.email
    }

@app.get("/me")
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    # 1. Decode the token to get the email
    import security
    payload = security.decode_access_token(token)
    email = payload.get("sub")

    # 2. Find the user in the DB
    user = db.query(models.Employee).filter(models.Employee.email == email).first()
    return {"full_name": user.full_name, "email": user.email, "status": "Authenticated"}
   '''