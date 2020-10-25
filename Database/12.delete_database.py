'''
Ending Topics:

1. Delete Database
2. Create function and class to use them
3. What next
    1. Few more important libarys
    2. Excercise code basic to advance
    3. Project discussion and work flow
    4. Interview Prepration:
        1. Resume
        2. Platforms
        3. Right call
        4. Right Job
'''

# create connection
import mysql.connector as con

mydb = con.connect(host='localhost', user='root', password='')

mycursor = mydb.cursor()

# delete database
# mycursor.execute('CREATE DATABASE heysushil_demo')
# mycursor.execute('DROP DATABASE heysushil_demo')

# create funciton for deleting database

class DBClass:
    def deleteDatabase(self):
        mycursor.execute('SHOW DATABASES')
        for db in mycursor:
            print('Database : ', db[0])

        # DELETE DATABASE
        dbname = input('Enter database name jo delete karna hai: ')
        mycursor.execute('DROP DATABASE IF EXISTS ' + dbname)

# call deelteDatabse
myobj = DBClass()
myobj.deleteDatabase()
# deleteDatabase()

'''
Excercise:

1. student name se table bano iske andar:
    Following fields de sakte hain:
        no
        roll_number
        name
        fathername
        mothername
        class
        mobile
        email
        registration_date

2. Marks name se table bano:
    followind files
        no
        roll_number
        hindi
        english
        sci
        math

3. At last table bane ke bad kuch function bana hain aur unka work kuch ye hoga:

    1. new student registration
    2. add student marks
    3. show result
        1. number abhi update 
    4. delete studnet with student detaila and marks also
'''