# for loop
# list tuple set dict

# this is list value
user = ['ram','shyam','ravi','geeta']

# this is dict values
user = {'name':'ram','course':'python'}
# print('\nUser: ',user)
for u in user:
    # print('\nWelcome, ',u)
    print('Your ',u,' : ',user[u])

# break: 
user = ['ram','shyam','ravi','geeta']
for u in user:    
    # use condtion to berak any specific point of loop
    if u == 'ravi':
        # break
        # continue skitp the current finded value
        continue
    
    print('\nHi, ',u, 'I am present')


# range(start,end,diff)
for r in range(2,21,2):
    print(r)
else:
    print('Our table is ended')    


# nested loop: 
'''

1stLoop[1 to 5]
    1stInnerLoop[1 to 5]
        1stInnerLoop[1 to 5]
'''

# range of 5 will start at 0 and end at 4
for r in range(5):
    # print(r)
    for u in range(5):
        # print(r, u)
        for i in range(5):
            print(r,u,i)
    # print('\n')
'''
r=0,1
    u=0,1,2,3,4
        i=01234 5
        i1=01234
        .
        .
        i4=01234

'''

for i in range(5):
    pass

'''
Programs:

1. get a user input and print a table of user given number.
2. print a 2 level for loop in which outer loop range given by user and inner loop range self give.
'''