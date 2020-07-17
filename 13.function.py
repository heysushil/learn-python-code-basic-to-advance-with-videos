# fucntion
# Type of fucntion: 2
'''
1. Pre-define:
    print()
    if()
    for()

2. user defin fucntion
    def functionName():
        function ki body
'''

# function define
def newFunction():
    print('\nhi function')

# fucntion call: after fucntion defin it must to call fucntion
newFunction()

# how many fucnton behaviours:

'''
1. function without argument and withour return value
2. function with argument and with return value
3. function without argument and return value
4. function with argruent and without return value

Argrument: it's like variable which holds value which is pass by the fucntion call and the arguments are recived on fucntion define box.

Return: return alvas return a single value or return a boolean value
'''

# 2 number fun behavour

# when define a argument in funciton box that means fucntion with argument. and in this case function have single argument
def studentAttendens(name, name2):
    # print('Hello studentAttendens funciton')
    return True

# after fucntion defining need to call it for output
# when function return a value which is get by the fucntion call
# print(studentAttendens('Neha','Sachin'))
if studentAttendens('Neha','Sachin') == True:
    print('YEs Neha and Sachin both are presne.')
else:
    print('Non one present')

# 3 fucntion behavour
def singleUser(name):
    print('Hi ',name,' . how are you?')

# call fucntion
singleUser('Neha')    


# 4th fucntion behavour
def otherUser():
    return False

# call fucntion
if otherUser() == True:
    print('Yes, otheruser fucntion successfully called')
elif otherUser() == False:
    print('THis time otheruser not available.')
else:
    print('Oh no otheruser didnt reapyed my anser. ')


# fucntion with unexprext numer of arguments
def studentCheckFucntion(*stu):
    # print('Hi ',stu[0],' ',stu[1],' ',stu[2])
    if 'seeta' in stu:
        print('Yes seeta is present')

studentCheckFucntion('ram','syam','seeta')

# dict ke form me value revice
def keyFucntion(**user):
    print('Hi ',user['name'])

keyFucntion(name='Ram',course='python')

# allot adefault value to fucnton argu.
def username(name='Default'):
    print('hi username ',name)

username('Mr. Ram')


# pass
def userRegistration():
    pass

# pass a list to function
def fucntionWIthList(listvalue):
    print('This is our list: ',listvalue)

# creat list wihcih pass to fucntion
listvalue = ['ram','shyam','geeta','seeta']    

fucntionWIthList(listvalue)

'''
Programm:

1. creat a fucntion in which you recive your friends list with the help of user input and in this case ou need to use list and append method of list . so that multiple user input will add to the list and at fincal show the friends name wich greating in function.

2. creat a fucntion in which you will use your preivioues firendslist and chek if you enter any name by useing input and if the name is exists in your firend list then you will show the message like: Great firendname , you are pressen in my tparty thank you for taht. otherwise if the friend name not exists in firend list then show the massage: Ohh no friendname is not came to my part.

3. creat a fucntion in which you will pass your all persanal details like: name email phone cours addres etc... .and recive them useing dict type on fucntion and show all your detials using multi line stirng on proper way.

4. fucntion numner3 which you created in fucntion behivour like fucntion with arguemnt and without return value but in this case you neet to use retun and show all the values outside of the fucniton.
'''