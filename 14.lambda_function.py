# lambda
'''
About Lambda function:

1. lambda function is also known as anonymous fucntion
2. ye signle line function
3. isme multiple arguments recive kar satkte hain but expresss hamesa single hoga
4. funciton ke andar function use karna hai tab hum lambda ka use kar sakte hai
5. filter() ya map() funciton ke sath iska use jada hota hai
6. ye kisi fucntion ke liye as a argument hota hai.

Syatax:

lambda arguments : expression
'''

# noraml lambda fucntion
lamvalue = lambda a, b, c : a * b * c

# finally print the lamvlaue but rember our lambda fucniton is stored in lamvalue
print('\n Our lamvalue: ',lamvalue(10,10,2))

# normal fucntion to done the same
def myfun(a,b,c):
    answer = a*b*c
    print('\nMyfun answer: ',answer)

myfun(10,10,10)

# in normal fucntion use lambda function
def user(num):
    return lambda a: a + num
    # print('\nAnswer: ',answer(50))

# remebder in this case at fisert we will call user fucntion
answer = user(10)
print('\nAnswer: ',answer(500))

# lambda using filter: for filttering use list and filter method
# to find out evern number from list using filter and lambda
mylist = [1,2,3,4,56,7,8,9,90]
evenNumList = list(filter(lambda number : (number%2 != 0), mylist))
print('\nOur even list: ',evenNumList)
# for num in mylist:

# map() fucntion useing to get double all list values
doubleMyListValues = list(map(lambda number : number * 2, mylist))
print('\nDoble values list: ',doubleMyListValues)

'''
Program:

1. using lambda fucntion get a result of addintion, subtraction and multiplication but remeber in these 3 caes you must take 2 arguments by user inpur and recive them frist argment normal function and in the normal fucntion you will have lambda which is recive secnond arguments and lambda fucntion finally perform the mathematical expression.

2. create a funciton in which you well recive list of multiple numbers and find the even number set and odd number set using fillter then show the bothe results using output fucntion in this care you must pass the output using return and recive it in output fucniton then show the resutl and then use the output of even and odd to use in another fucniton and subtact even list with odd list.
'''