"""
Main routes for app
"""

import os
from fastapi import FastAPI, APIRouter
import sqlalchemy
import psycopg2
import pandas as pd
from app.db import get_db_connection

router = APIRouter()


"""
This file is for containing the basic routes of the API
"""


@router.get('/dbtest')
async def dbtest():
    """
    TEST ROUTE:
    This is a test hook for the API that will return the results of a sql query against the db
    to return the table names.
    """
    # Obtain a connection
    conn = get_db_connection()
    # Create the cursor object
    cur = conn.cursor()
    query = """
        SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';
        """
    # Execute the query on the db   
    cur.execute(query)

    # Return the query results
    return cur.fetchall()


@router.get('/test')
async def test():
    """
    TEST ROUTE:
    This hook is for testing a call on the case table and returning all the results
    """
    # Obtain a connection
    conn = get_db_connection()
    # Create the cursor object
    cur = conn.cursor()
    query = """SELECT * FROM public.case;
            """
    # Execute the query
    cur.execute(query)

    # Return the query results
    return cur.fetchall()
    

    


