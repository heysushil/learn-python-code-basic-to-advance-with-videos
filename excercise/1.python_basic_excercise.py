'''
Python excercise list 2 with Hey Sushil:

1. Jiasa likha hai waise hi output me show karna hai? Hint: str
2. Python ya PIP ka version kaise pata kare? Hint: cmd command
3. Kisi library ko kaise import karenge? Kaise current date dekhe?
4. Apna first and last name print karna hai, but pahle last then first name kaise?
5. multipal numbers ko comma sepereted lena hain and list aur tuple me show karana hai? Hint: str split()
6. Kisi bhi string ko kaise tode aur usme se specific content kaise get kare? Hint: str split()
7. Kisi bhi list mese first aur last value kaise show kiya jaye? Hint: positiv negative
8. Kisi date me kaise . ya / ki jagh kuch aur replace kiya jaye? Hint: direct or replace
9. Python built in function ki discription kaise jaane?
'''

# 1. Jiasa likha hai waise hi output me show karna hai? Hint: str
mymessage = '''
6. Kisi bhi string ko kaise tode aur usme se specific content kaise get kare? Hint: str split()
    7. Kisi bhi list mese first aur last value kaise show kiya jaye? Hint: positiv negative
        8. Kisi date me kaise . ya / ki jagh kuch aur replace kiya jaye? Hint: direct or replace
            9. Python built in function ki discription kaise jaane?
'''
print('\n', mymessage)

# 2. Python ya PIP ka version kaise pata kare? Hint: cmd command

# 3. Kisi library ko kaise import karenge? Kaise current date dekhe?
import datetime as d

print('\nCurrent date and time: ', d.datetime.now())

# 4. Apna first and last name print karna hai, but pahle last then first name kaise?

first = 'Hey'
last = 'Sushil'
print('\nName' + last + first)

# 5. multipal numbers ko comma sepereted lena hain and list aur tuple me show karana hai? Hint: str split()

multipalNumber = input('\nEnter multipal numebrs with comma seprated: ')
print('\nmultipalNumber: ', multipalNumber)
mylist = multipalNumber.split(",")
print('\nmylist type: ', type(mylist), ' : ', mylist)
print('\nConvert in tupel: ', tuple(mylist))

# 6. Kisi bhi string ko kaise tode aur usme se specific content kaise get kare? Hint: str split()
friends = input('\nEnter your file name: ')
# first split the file name
fileExtenstion = friends.split('.')
print('\nfileExtenstion: ', fileExtenstion)
print('\nFile externstion is: ', fileExtenstion[-1])
print('\nFile externstion by repr(): ', repr(fileExtenstion[-1]))

# 7. Kisi bhi list mese first aur last value kaise show kiya jaye? Hint: positiv negative

# 8. Kisi date me kaise . ya / ki jagh kuch aur replace kiya jaye? Hint: direct or replace 12-01-2020 , 12,01,2020

mydate = '12-01-2020'
print('\nMy version of date: ', mydate.replace('-', '/'))

mydate = (12,11,2020)
print('\nMy new way of date formate: %f/%f/%i'%mydate)

# 9. Python built in function ki discription kaise jaane?

print('\nDetail of abs method: ', abs.__doc__)