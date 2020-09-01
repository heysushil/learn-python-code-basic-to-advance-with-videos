import installing_and_connecting_db as con

# creating form for adding day wise spends on table
'''
goods_name
price
dates
person
'''

dates = input('Enter current date: ')
person = input('Enter your name: ')
goods_name = input('Enter goods name: ')
price = int(input('Enter goods price: '))

# user curser to run commit sql query
sql = "INSERT INTO aug_month (dates, person, goods_name, price) VALUES ('{}', '{}', '{}', '{}')".format(dates, person, goods_name, price)
# need to execute it
con.mycursor.execute(sql)

# jab bhi table me values modification ya insert ki baaat ho to commit() method ko call karna jaruri hai otherwise databse table me valeus store nahi hongi.
con.mydb.commit()

# check row of update on table
print('\nRow update number: ', con.mycursor.rowcount)

print('\nRow update number: ', con.mycursor.lastrowid)