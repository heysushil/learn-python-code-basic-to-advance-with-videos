# list
# index []
x = 746473
listval = [1,2,3,4,5,6]
print(type(listval))
# list ki indexing wo 0 se start hoti
print(listval[1])

listval = ['hello','7637',8383738,'python']
print(listval[0:3]) #n-1
# posstive aur negative / range isme hame hamesa 2 pont milee hain.
# start aur end
print('\nOnlye start point give: ',listval[2:])
print('End pint given: ',listval[:4]) #n-1
print('Give single number: ',listval[3])
print('Negatve postion: ',listval[-3:-1])

'''
List
    new value add
    existing value change 
    existing value detele
    list delete
'''

# list methods
# add new value from last possition
listval.append('New vale')

# store list to new list
listval1 = listval
listval2 = listval.copy()

listval1.clear()
del listval1
listval2.append('hello')
listval2.append('hello')

listval = [4343,2452,4563,34563]
print('count list: ',listval2.count('hello'))
listval2.extend(listval)
# print(listval2.)
print(listval2.index(4343))
print('pop: ',listval2.pop(5))
print('remove: ',listval2.remove('python'))
listnum = [4,6,2,8,9,3,2,4]
liststr = ['asdf','sdaf','fhkjfhd']
listnum.sort()
print('sor: ',listnum)
listnum.reverse()
print('sort: ',listnum)
print('Final list: ',listval2)


'''
Excersice:

1. program banao jisme user se input le ke usko ek list me add karna hai aur final uska output show karana hai. is lise me kewal minimum 5 user ke name input kar ke unko show karna hai.

2. jo user list banaya hai usme se agar user kisi index position ki value ko delet karna chata hai to user input se index possition le ke use vaue ko list se delte karke final list ka output show karana hai.

3. current list ka use karke agar user koi name enter karta hai aur wo exist karta hai to wo name show karna hai other wise ek name not fount ka messaage show karna hai?

4. current list me user ye pata karna chata hai ki koi name kitni baar exist kar raha hai. agar user ne jo name enter kiya hai wo ek baar se jada bar hai to message show karna hai ki wo name total kitni bar hai list me otherwise normal message show karna hai ki name kewal ek baar hi list me exist karta hai.

5. current list ka use karke user ko koi name search karna hai aur agar wo name list me hai to user ko wo name delete karna hai.

6. current list me mohan, sohan, ram, syam ko add karna hai aur inko finally assending order me sort karke output show karan hai. iske liye uper code me dekh lena ki sorting kaise ki gai hai.
'''

