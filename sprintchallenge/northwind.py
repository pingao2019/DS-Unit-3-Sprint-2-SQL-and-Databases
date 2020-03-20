import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

"""What are the ten most expensive items (per unit price) in the database?")"""
curs.execute("""
SELECT ProductName, UnitPrice 
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10
""").fetchall()


"""What is the average age of an employee at the time of their hiring? (Hint: a lot of arithmetic works with dates.)")"""
curs.execute("""
SELECT AVG(HireDate - BirthDate) 
FROM Employee
""").fetchall()

"""How does the average age of employee at hire vary by city?"""
curs.execute("""
SELECT City, AVG(HireDate - BirthDate) 
FROM Employee
GROUP BY City
""").fetchall()


