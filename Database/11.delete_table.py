# create new table by funciton

import installing_and_connecting_db as con
mycursor = con.mydb.cursor()

# create new table
'''
Table funciton:

1. table name to ek hai so isko same as sdelete me tablename jaise use kiya ja sakta hai.
2. yaha par table me multipal keys hain aur usne datatypes hain.
'''
mycursor.execute('CREATE TABLE IF NOT EXISTS demotable(sr INT(10) NOT NULL AUTO_INCREMENT PRIMARY KEY, goods_name VARCHAR(250), price INT(8), dates VARCHAR(12), person VARCHAR(100))')

# TABLE delete karne ke liye hum drop keyword 
# mycursor.execute('DROP TABLE demotable')

# craete function for deleting table
def deleteDBTable():
    print('\nYe sabhi table ke names hain: \n')
    mycursor.execute('SHOW TABLES')
    for t in mycursor:
        print(t[0])

    tableName = input('\nEnter table name jisi delete karna hai: ')
    mycursor.execute('DROP TABLE ' + tableName)


deleteDBTable()
