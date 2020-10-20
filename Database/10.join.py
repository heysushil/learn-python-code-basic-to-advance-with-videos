'''
Table joining in MySQLi database:

1. inner join: comman data form both table
2. left join: get left table all data 
3. right join: get right table all data


Example:

Month kharche ke liye aug month ka table create kiya.

table student
    sr
    rn
    name
    class

table subject_marks
    sr
    rn
    math
    hindi
    english

table result
'''

import installing_and_connecting_db as con

mycursor = con.mydb.cursor()

# studnet table
mycursor.execute('CREATE TABLE IF NOT EXISTS students(sr INT(10) NOT NULL AUTO_INCREMENT PRIMARY KEY, rn INT(5), name VARCHAR(100), class VARCHAR(50))')

# studnet subjects
mycursor.execute('CREATE TABLE IF NOT EXISTS subjects(sr INT(10) NOT NULL AUTO_INCREMENT PRIMARY KEY, rn INT(5), math VARCHAR(100), hindi VARCHAR(50), english VARCHAR(50))')

# # inset data on student
# rn = int(input('Enter roll number: '))
# name = input('Enter your name: ')
# classname = input('Enter class name: ')

# # user curser to run commit sql query
# sql = "INSERT INTO students (rn, name, class) VALUES ('{}', '{}', '{}')".format(rn, name, classname)
# # need to execute it
# con.mycursor.execute(sql)

# con.mydb.commit()

# # check row of update on table
# print('\nRow update number: ', con.mycursor.rowcount)

# print('\nRow update number: ', con.mycursor.lastrowid)



# add marks to student
# rn = int(input('Enter roll number: '))
# math = input('Enter math number: ')
# hindi = input('Enter hindi number: ')
# english = input('Enter english number: ')

# # user curser to run commit sql query
# sql = "INSERT INTO subjects (rn, math, hindi, english) VALUES ('{}', '{}', '{}', '{}')".format(rn, math, hindi, english)
# # need to execute it
# con.mycursor.execute(sql)

# con.mydb.commit()

# # check row of update on table
# print('\nRow update number: ', con.mycursor.rowcount)

# print('\nRow update number: ', con.mycursor.lastrowid)


# get 2 table data using joing
# con.mycursor.execute("SELECT students.*, subjects.* FROM students JOIN subjects ON students.rn = subjects.rn")

# 1. inner join: comman data form both table
con.mycursor.execute("SELECT s.rn, s.name, s.class, sub.math, sub.hindi, sub.english FROM students s INNER JOIN subjects sub ON s.rn = sub.rn")

all_data = con.mycursor.fetchall()

print('\nInner join data')
for i in all_data:
    print(i)


# lef join
con.mycursor.execute("SELECT s.rn, s.name, s.class, sub.math, sub.hindi, sub.english FROM students s LEFT JOIN subjects sub ON s.rn = sub.rn")

all_data = con.mycursor.fetchall()

print('\nLeft join data')
for i in all_data:
    print(i)


# right join
con.mycursor.execute("SELECT s.rn, s.name, s.class, sub.math, sub.hindi, sub.english FROM students s RIGHT JOIN subjects sub ON s.rn = sub.rn")

all_data = con.mycursor.fetchall()

print('\nRight join data')
for i in all_data:
    print(i)