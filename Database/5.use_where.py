import installing_and_connecting_db as con

# create condtion to check user input is int value or not
getData = input('Enter number to get data of that row: ')

if getData.isdigit() == True:
    print('\nI get right id for furter proced.')

    # get id to seach data on table
    query = "SELECT * FROM aug_month WHERE sr='{}'".format(getData)
    con.mycursor.execute(query)
    result = con.mycursor.fetchall()
    if result == []:
        print('\nYou get noting on this id. Try another.')
    else:
        print('\nGet result: ', result)
elif getData.isalpha() == True:
    query = "SELECT * FROM aug_month WHERE person LIKE '%{}%'".format(getData)
    con.mycursor.execute(query)
    result = con.mycursor.fetchall()
    if result == []:
        print('\nYou get noting on this id. Try another.')
    else:
        print('\nGet result: ', result)
else:
    print('\nWrong input pleas try again!')