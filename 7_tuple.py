'''
Tuple

List: changable = []
Tuple: Non-chanbel = ()
'''

# tuple
t = ()

# jabhi single value tuple me ho to value ke bad e comma dena jaruri hai
t = ('Python',)

# output
print('\n\nt type: ',type(t))


# t fill with more value
t = ('Python','PHP','Java','.Net','C')

print('\nt values: ',t)

# tuple me slicing and indexing
print('t[0]: ',t[0])
print('t[2:]: only provide starting point = ',t[2:])
# jab bhi slicing me end point dete hai to wo n-1 posstion tak chalta hai
print('t[:4]: ',t[:4])
print('t[2:4]: start and end point: ',t[2:4])
print('t[-3:-1]: ',t[-3:-1])

# tuple me values to modify karna
l = list(t)
print('tuple conver in list: ',type(l))
l.append('C++')
l.append('Cobol')
l.append('Perl')
print('\nL values: ',l)

# conver list into tuple
t = tuple(l)
print('\nt type: ',type(t))
print('\nt values: ',t)

# del: ye del kisi ko bhi delete kar sakta hai
newt = t
print('\nnewt value: ',newt)
del newt
# print('\nnewt del: ',newt)

# join karne ke liye + (concatanation ka use hota hai)
y = t
addtuple = t + y
print('\naddtuple values: ',addtuple)

# count
print('\ncount python: ',t.count('Python'))

# index
print('\nindex: ',t.index('PHP'))

# * (multiplication)
n = t * 2
print('\n n vlaues: ',n)

# in ye membership operatior hai
print('\nuse in: ','PHP' in t)

# length find out
print('len: ',len(t))

# cmp(): compare
# compare = cmp(t, y)
# print('\ncmp(): ',cmp(3, 4))

# min and max
n = (1,2,3,4,5)
print('min: ',min(n))
print('max: ',max(n))


'''
Program:

1. ek friend list bana hai tuple me aur usko multiline stirng ka use kar ke show karna hai

2. previuse friend list me kuch firends ko hata kar new friends ke name add karne hain aur output show karan hai

3. user se number ka input lena hai aur usko list me add karna hai iske baad usko non changable bana hai aur variablem me max number and min umber findout karke show karna hai.
'''


