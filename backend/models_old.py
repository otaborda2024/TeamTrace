'''

import datetime
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Boolean
import database

# 1. Employees Table (Required for Week 2 Auth)
class Employee(database.Base):
    __tablename__ = "employees"
    
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False) # For secure login
    role=Column(String, default="employee")
    is_active = Column(Boolean, default=True)

# 2. Job Sites Table
class JobSite(database.Base):
    __tablename__ = "jobsites"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    radius_meters = Column(Float, default=100.0) # Geofence size

# 3. Sessions (Check-in/Check-out) Table
class Session(database.Base):
    __tablename__ = "sessions"
    
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=False)
    job_site_id = Column(Integer, ForeignKey("job_sites.id"), nullable=False)
    check_in_time = Column(DateTime, default=datetime.datetime.utcnow)
    check_out_time = Column(DateTime, nullable=True)

# 4. Location Logs Table
class LocationLog(database.Base):
    __tablename__ = "location_logs"
    
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

# 5. Alerts Table
class Alert(database.Base):
    __tablename__ = "alerts"
    
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=False)
    job_site_id = Column(Integer, ForeignKey("job_sites.id"), nullable=False)
    alert_type = Column(String, nullable=False) # e.g., "Left Geofence"
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

    '''
    