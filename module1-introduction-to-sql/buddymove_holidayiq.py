# module1-introduction-to-sql/buddymove_holidyiq.py
#- Count how many rows you have - it should be 249!
#- How many users who reviewed at least 100 `Nature` in the category also
#  reviewed at least 100 in the `Shopping` category?
#- (*Stretch*) What are the average number of reviews for each category?

import pandas as pd
import sqlite3
import os

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..","module1-introduction-to-sql","buddymove_holidayiq.sqlite3")

conn = sqlite3.connect(DB_FILEPATH)
curs = conn.cursor()

df = pd.read_csv("https://github.com/pingao2019/DS-Unit-3-Sprint-2-SQL-and-Databases/blob/master/module1-introduction-to-sql/buddymove_holidayiq.csv")

df.to_sql("buddymove_holidayiq", con=conn, if_exists='replace')

#- Count how many rows you have - it should be 249!
query1 = """
SELECT
	count(distinct "User Id") as Rows 
FROM buddymove_holidayiq
"""
row = curs.execute(query1).fetchone()
print ("Total Number of Rows:")
print(row[0])


# How many users who reviewed at least 100 Nature in the category
# also reviewed at least 100 in the Shopping category?
query2 = """
SELECT
	count(distinct "User Id") as Rows 
FROM buddymove_holidayiq
WHERE Nature >= 100 AND Shopping >= 100
"""
row = curs.execute(query2).fetchone()
print ("Number of Nature/Shopping Lovers:")
print(row[0])


# What are the average number of reviews for each category?
query2 = """
SELECT
	AVG(Sports) as "Sports Average"
	, AVG(Religious) as "Religious Average"
	, AVG(Nature) as "Nature Average"
	, AVG(Theatre) as "Theatre Average"
	, AVG(Shopping) as "Shopping Average"
	, AVG(Picnic) as "Picnic Average"
FROM buddymove_holidayiq
"""
row = curs.execute(query2).fetchall()
print ("Averages:")
categories = ['Sports','Religious','Nature','Theatre','Shopping','Picnic']
for i in range(6):
    print(categories[i], ":", row[0][i])

conn.commit()