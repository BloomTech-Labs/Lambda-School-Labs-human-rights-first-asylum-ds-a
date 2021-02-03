"""Database functions"""

import os
import pandas as pd
from dotenv import load_dotenv
from fastapi import APIRouter, Depends
import sqlalchemy
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base
import psycopg2

router = APIRouter()
Base = declarative_base()

"""
This file will contain functions, classes, and logic regarding the database connection to the AWS RDS Database.
It will define the two classes, Case() and Judge(), that will be used to construct records for 
sending to store on the db.

It will also contain the function for obtaining the connection to the database.
"""

# Import environment variables for connecting to the db
def get_db_connection():
    """
    FUNCTION: When called, will return a connection to the AWS RDS database
    being used for the HRFAsylum project

    RETURNS: Database Connection
    """
    # Credentials for connecting to the database
    rds_username = os.getenv('rds_username')
    rds_password = os.getenv('rds_password')
    rds_endpoint = os.getenv('DATABASE_URL')
    port = '5432'
    database_name = 'hrfasyluma'
    
    
    return psycopg2.connect(host=rds_endpoint, user=rds_username, password=rds_password)

"""
Define the classes used for constructing database objects for storing within the aws rds db
"""

class Case(Base):
    """
    Class for defining a database object for inserting into the database in the table 'Case'
    """
    __tablename__ = 'case'

    id = Column(Integer, primary_key=True)
    column_id = Column(Integer)
    case_url = Column(String(250))
    court_type = Column(String(250))
    hearing_type = Column(String(250))
    credibility_of_refugee = Column(String(250))
    refugee_origin = Column(String(250))
    hearing_location = Column(String(250))
    protected_ground = Column(String(250))
    hearing_date = Column(Date)
    decision_date = Column(Date)
    social_group = Column(String(250))
    judge_id = Column(Integer)

class Judge(Base):
    """
    Class for defining a database object for inserting into the database in the table 'Case'
    """
    __tablename__ = 'judge'

    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    trump_appointed = Column(Boolean)  
    date_appointed = Column(Date)
    county = Column(String(250))
    birth_date = Column(Date)
    biography = Column(String(250))

