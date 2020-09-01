import installing_and_connecting_db as con

# sql query run by execute method
con.mycursor.execute("SELECT * FROM aug_month")

all_data = con.mycursor.fetchall()

# print('\nCheck all data: ', all_data)

# get data on for loop
# (2, 'Bread', 10, '01/09/2020', 'Hey Sushil')

welcome_message = '''
    -------------------------------------------
        Hi, Guest yout August Month Expences
    -------------------------------------------
    No  Name        Goods Name      Price       Date
    -------------------------------------------
'''
print(welcome_message)
for data in all_data:
    # print('\nData: ', data[1])
    single_data = '''
    {0}  {4}  {1}       {2}         {3}
    '''.format(data[0], data[1], data[2], data[3], data[4])
    print(single_data)

# select spicific columns from table
con.mycursor.execute("SELECT person, goods_name, price FROM aug_month")

# all_data = con.mycursor.fetchall()

# print('\nAll specif data: ', all_data)

# get single row data
all_data = con.mycursor.fetchone()

print('\nAll specif data: ', all_data)