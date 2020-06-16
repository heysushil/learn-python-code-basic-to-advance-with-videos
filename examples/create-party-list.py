print('Welcome to the Party List Creater paltform')

# Get number of party members
try:
    partyMembersNumber = int(input('Enter Number of Party Members: '))

    if partyMembersNumber > 0:
        print('Thanks for varifying the partymemeres number. \n\nYour party have {} members right.\n\nIf its right click y other wise n'.format(partyMembersNumber))
        # verify the memebrs
        yn = input('Enter y/n: ')
        if yn == 'y':
            print('Greate you verifyed your party members numebr. Lets create the list.')

            # create list of party members
            partyMembers = []
            for 
        else:
            print('You want to change party memebres number. Lets start again with new numbers')
except:
    print('Only Numbers are allowed try again.')
