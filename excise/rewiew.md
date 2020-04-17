This study guide should reinforce and provide practice for all of the concepts you have seen in the past week. There are a mix of written questions and coding exercises, both are equally important to prepare you for the sprint challenge as well as to be able to speak on these topics comfortably in interviews and on the job.

If you get stuck or are unsure of something remember the 20 minute rule. If that doesn't help, then research a solution with google and stackoverflow. Only once you have exausted these methods should you turn to your Team Lead - they won't be there on your SC or during an interview. That being said, don't hesitate to ask for help if you truly are stuck.

Have fun studying!


# SQL

## Questions of understanding
1. What is SQL?
2. What is a RDBMS?
3. What is the ETL pipeline?ETL pipeline refers to a set of processes extracting data from one system, transforming it, and loading into some database or data-warehouse. ... Another type of a data pipeline that is an ETL pipeline, is an ELT pipeline: loading all of your data to the data warehouse, and transforming it only later


4. What is a schema?
5. What does each letter in ACID stand for? Give an explanation for each and why they matter?
 ACID - Atomicity, Consistency, Isolation, Durability - a set of guarantees provided by the use of transactions to ensure that data is always in a valid state, even if e.g. a query inserting new data is interrupted by a failure of any sort (including external to the system such as a power outage).

    Atomicity: a transaction functions as a “unit” - it either succeeds completely, or fails completely
    Consistency: transactions can only change a database from a valid state to another valid state
    Isolation: concurrent transactions are isolated from each other, so they have the same results as if they were run sequentially
    Durability: once a transaction has finished it will survive runtime system failure (it is recorded in non-volatile memory)

6. Explain each of the table relationships and give an example for each
 - One-to-One
 - One-to-Many :A one-to-many relationship in a database occurs when each record in Table A may have many linked records in Table B, but each record in Table B may have only one corresponding record in Table A
 - Many-to-Many:  many-to-many relationship refers to a relationship between tables in a database when a parent row in one table contains several child rows in the second table, and vice versa. 

## Syntax
For the following section, give a brief explanation of each of the SQL commands.

1. **SELECT** - 
2. **WHERE** - 
3. **LIMIT** - 
4. **ORDER** -
5. **JOIN** -
6. **CREATE TABLE** - 
7. **INSERT** -
8. **DISTINCT** -
9. **GROUP BY** -
10. **ORDER BY** -
11. **AVG** - 
12. **MAX** -
13. **AS** -

## Starting From Scratch
Create a file named `study_part1.py` and complete the exercise below. The only library you should need to import is `sqlite3`. Don't forget to be PEP8 compliant!
1. Create a new database file call `study_part1.sqlite3`
2. Create a table with the following columns
```
 student - string
 studied - string
 grade - int
 age - int
 sex - string
 ```
create_ta ble= '''CREATE TABLE student1(student varchar(25) primary key,
  studied varchar(25),
 grade INT,
 age INT,
 sex varchar(10)
)'''
3. Fill the table with the following data
```
 'Lion-O', 'True', 85, 24, 'Male'
 'Cheetara', 'True', 95, 22, 'Female'
 'Mumm-Ra', 'False', 65, 153, 'Male'
 'Snarf', 'False', 70, 15, 'Male'
 'Panthro', 'True', 80, 30, 'Male'
 ```
students= '''INSERT INTO student1(student, studied, grade, age, sex) 
values ('Lion-O', 'True', 85, 24, 'Male'),
 ('Cheetara', 'True', 95, 22, 'Female'),
 ('Mumm-Ra', 'False', 65, 153, 'Male'),
 ('Snarf', 'False', 70, 15, 'Male'),
 ('Panthro', 'True', 80, 30, 'Male');'''

conn.commit()

4. Save your data. You can check that everything is working so far if you can view the table and data in DBBrowser
5. Write the following queries to check your work. Querie outputs should be formatted for readability, don't simply print a number to the screen with no explanation, add context.
```
What is the average age? Expected Result - 48.8
What are the name of the female students? Expected Result - 'Cheetara'
How many students studied? Expected Results - 3
Return all students and all columns, sorted by student names in alphabetical order.
```
query_age= '''SELECT AVG(age)
FROM table_1;'''
print('avarage age', curs.excute(query_age)


query_name = '''SELECT student
FROM table_1 
where sex = 'Female';'''
print("name of female:", curs.excute(query_name)

query_studied = '''SELECT count(studied)
FROM table_1 
where studied = 'Ture';'''
print("There are :", curs.excute(query_studied)

query_order = '''SELECT *
FROM table_1 
order by student;'''
print(curs.excute(query_order)

## Query All the Tables!

### Setup
Before we get started you'll need a few things.
1. Download the [Chinook Database here](https://github.com/bundickm/Study-Guides/blob/master/data/Chinook_Sqlite.sqlite)
2. The schema can be [found here](https://github.com/bundickm/Study-Guides/blob/master/data/Chinook%20Schema.png)
3. Create a file named `study_part2.py` and complete the exercise below. The only library you should need to import is `sqlite3`. Don't forget to be PEP8 compliant!
4. Add a connection to the chinook database so that you can answer the queries below.

### Queries
**Single Table Queries**
1. Find the average invoice total for each customer, return the details for the first 5 ID's
2. Return all columns in Customer for the first 5 customers residing in the United States
3. Which employee does not report to anyone?
4. Find the number of unique composers
5. How many rows are in the Track table?

**Joins**

6. Get the name of all Black Sabbath tracks and the albums they came off of
7. What is the most popular genre by number of tracks?
8. Find all customers that have spent over $45
9. Find the first and last name, title, and the number of customers each employee has helped. If the customer count is 0 for an employee, it doesn't need to be displayed. Order the employees from most to least customers.
10. Return the first and last name of each employee and who they report to

# NoSQL

## Questions of Understanding
1. What is a document store?
2. What is a key:value pair? What datatype in Python uses Key:Value pairs?
3. Give an example of when it would be best to use a SQL Database and when it would be best to use a NoSQL Database
4. What are some of the trade-offs between SQL and NoSQL?
5. What does each letter in BASE stand for? Give an explanation for each and why they matter?
 - B
 - A
 - S
 - E