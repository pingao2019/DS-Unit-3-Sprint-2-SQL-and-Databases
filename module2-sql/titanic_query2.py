import os
import json
import psycopg2
from dotenv import load_dotenv
from psycopg2.extras import execute_values
import pandas

# adds the contents of the .env file to our environment
# looking in the .env file for env vars
load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

#
# CONNECT TO THE DB!
#

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print(type(connection)) #> <class 'psycopg2.extensions.connection'>

cursor = connection.cursor()
print(type(cursor)) #> <class 'psycopg2.extensions.cursor'>

#
# MAKE A TABLE!
#
# columns: Survived,Pclass,Name,Sex,Age,Siblings/Spouses Aboard,Parents/Children Aboard,Fare

table_creation_query = """
DROP TABLE IF EXISTS passengers;
CREATE TABLE IF NOT EXISTS passengers (
  id SERIAL PRIMARY KEY,
  survived bool,
  pclass integer,
  name varchar NOT NULL,
  gender varchar NOT NULL,
  age float,
  sib_spouse_count integer,
  parent_child_count integer,
  fare float
);
"""
cursor.execute(table_creation_query)




#
# READ THE CSV FILE! AND MAYBE TRANSFORM THE DATA
#



#
# INSERT DATA INTO THE TABLE
#






# ACTUALLY SAVE THE TRANSACTIONS
# if creating tables or inserting data (changing db)
connection.commit()
