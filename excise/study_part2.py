

import os
import sqlite3
DB_FILEPATH ='chinook.db'
#DB_FILEPATH = os.path.join(os.path.dirname(_file_), "..", 'chinook.db')
conn = sqlite3.connect(DB_FILEPATH )
curs= conn.curse()
#1. Find the average invoice total for each customer, return the details for the first 5 ID's
result = curs.execute(''' SELECT * from customers;
  ''').fetchall()

print(result)

Avg_invoice_total= '''select CustomerId,AVG(Total)
FROM invoices
GROUP BY customerId
LIMIT 5;'''
print('Avarage invoice total', curs.excute(Avg_invoice_total).fetchall())
#2. Return all columns in Customer for the first 5 customers residing in the United States
customer_USA= '''select CustomerId,AVG(Total)
FROM invoices
GROUP BY customerId
LIMIT 5;'''
print('5 customer_USA', curs.excute(customer_USA).fechall())

#3. Which employee does not report to anyone?
employee_reportnull= '''select EmployeeId, LastName, FirstName
FROM employees
WHERE ReportsTo IS NULL;'''
print('employee does not report to anyone', curs.excute(employee_reportnull).fetchall())

#4. Find the number of unique composers

unique_composer='''SELECT COUNT(DISTINCT(Composer))
FROM tracks;'''

print('num_uniq_composers', curs.excute(unique_composer).fetchall())

#5. How many rows are in the Track table?
row_track='''SELECT COUNT(*)
FROM tracks;'''

print('The rows of track is ', curs.excute(row_track).fetchall())









