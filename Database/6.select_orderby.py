import installing_and_connecting_db as con

# select data from aut_month table by decending order
# order by sr
# con.mycursor.execute("SELECT * FROM aug_month ORDER BY sr DESC")

# order by person
# con.mycursor.execute("SELECT * FROM aug_month ORDER BY person DESC")

# with where and order by price desc
# con.mycursor.execute("SELECT * FROM aug_month WHERE person LIKE '%s%' ORDER BY price DESC")

# order by assending order
con.mycursor.execute("SELECT * FROM aug_month WHERE person LIKE '%s%' ORDER BY price ASC")

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
