import installing_and_connecting_db as con
mycursor = con.mydb.cursor()

def createTable():
    tablecolumn = int(input('\nEnter total number of comumb: '))
    usertable = []
    i = 0
    while i < tablecolumn:
        columnname = input('Enter colmun {} name: '.format(i+1))
        usertable.append(columnname)
        i += 1
    print('\nColumn names: ', usertable)
    exit()
    mycursor.execute('CREATE TABLE IF NOT EXISTS demotable(sr INT(10) NOT NULL AUTO_INCREMENT PRIMARY KEY, goods_name VARCHAR(250), price INT(8), dates VARCHAR(12), person VARCHAR(100))')

    print('\nList of tables: ')
    for t in mycursor.execute('SHOW TABLES'):
        print(t)

createTable()