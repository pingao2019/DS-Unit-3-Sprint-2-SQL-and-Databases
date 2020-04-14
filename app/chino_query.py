# app/chino_queries.py


import os
import sqlite3
DB_FILEPATH ='chinook.db'
#DB_FILEPATH = os.path.join(os.path.dirname(_file_), "..", 'chinook.db')


conn = sqlite3.connect(DB_FILEPATH )

curs= conn.curse()


result = curs.execute(''' SELECT * from customers;
  ''').fetchall()

print(result)















