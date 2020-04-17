import sqlite3


conn = sqlite3. connect('study_part1.sqlite3')
cur = conn.cursor()


create table study1(student VARCHAR(20).  )

import sqlite3

connection = sqlite3.connect('study_part1.sqlite3')
curs= connection.cursor()
table_1 = '''
CREATE TABLE table_1(
    student VARCHAR(20),
    studied VARCHAR(20),
    grade INT,
    age INT,
    sex VARCHAR(20)
);
'''
curs.execute(table_1)

insert_1 = '''
INSERT INTO table_1
    (student, studied, grade, age, sex) 
VALUES
    ('Lion-O', 'True', 85, 24, 'Male'),
    ('Cheetara', 'True', 95, 22, 'Female'),
    ('Mumm-Ra', 'False', 65, 153, 'Male'),
    ('Snarf', 'False', 70, 15, 'Male'),
    ('Panthro', 'True', 80, 30, 'Male');
'''

curs.execute(insert_1)
connection.commit()

query_age= '''SELECT AVG(age)
FROM table_1;'''
print('avarage age', curs.excute(query_age).fetchone())


query_name = '''SELECT student
FROM table_1 
where sex = 'Female';'''
print("name of female:", curs.excute(query_name).fetchall())

query_studied = '''SELECT count(studied)
FROM table_1 
where studied = 'Ture';'''
print("There are :", curs.excute(query_studied).fetchone())

query_order = '''SELECT *
FROM table_1 
order by student;'''
print(curs.excute(query_order.fetchone())
















