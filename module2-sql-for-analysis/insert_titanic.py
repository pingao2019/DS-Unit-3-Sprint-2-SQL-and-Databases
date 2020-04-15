# module2-sql-for-analysis/insert_titanic.py


import os
import sqlite3
import pandas as pd 
import psycopg2
from psycopg2.extras import execute_values
from dotenv import load_dotenv


# read in
DB_FILEPATH = os.path.join(os.path.dirname(__file__), 'titanic.csv')

df = pd.read_csv(DB_FILEPATH)


load_dotenv() # look in the .env file for env vars, and add them to the env
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)

print("CONNECTION:", connection)
cursor = connection.cursor()
print("CURSOR:", cursor)

for i in range(0,len(df)):
    values = list(df.itertuples(index=False, name=None))[i]

    insertion_query = f'''
    INSERT INTO titanic_table (Survived, Pclass, Name, Sex, Age, Siblings_or_Spouses, Parents_Children, Fare)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'''

    cursor.execute(insertion_query, values)
cursor.execute("SELECT * from titanic_table")
result = cursor.fetchall()
print("RESULT:", result)

connection.commit()