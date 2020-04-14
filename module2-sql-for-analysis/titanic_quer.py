# titanic_queries.py


import os
import sqlite3
import pandas as pd 
import psycopg2
from psycopg2.extras import execute_values
from dotenv import load_dotenv


# read in
DB_FILEPATH = os.path.join(os.path.dirname(__file__), 'titanic.csv')

df = pd.read_csv(DB_FILEPATH)



connection.commit()