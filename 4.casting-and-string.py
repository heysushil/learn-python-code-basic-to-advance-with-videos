# Hi, agar koi question or query ho to YouTube Channel par comment kar sakte ho otherwise mail me on heykyakaru@gmail.com
# YouTube Channel Link: https://www.youtube.com/channel/UCphs2JfmIClR62wbyf76HDg
# New updates ke liye visit

# Also contact for College Project & Project Report

# HEY KYA KARU यूट्यूब चैनल के जरूरी लिंक 
# 1. Python Basic and Advance ट्यूटोरियल प्लेलिस्ट https://www.youtube.com/playlist?list=PLK6wiPavf7QikS9PMYrGZXz1HlE1KZLD3
# 2. PHP Projects प्लेलिस्ट https://www.youtube.com/playlist?list=PLK6wiPavf7QiEj6IPc3lkjz1wR4w9RM6B
# 3. GitHubट्यूटोरियल प्लेलिस्ट  https://www.youtube.com/watch?v=LUyVs2MTlTM&list=PLK6wiPavf7Qjydpc5v-hdIoqCx2V19pHP
# 4. Python Project https://www.youtube.com/watch?v=3lrbbB38zpU&list=PLK6wiPavf7Qj-NLJhbkxw9QfonweHafcN
# 5. Tips and Trick for Programming: https://www.youtube.com/watch?v=vPL6ODrfcwI&list=PLK6wiPavf7QiVLYXrC2TW_fdcZp57MgMB

'''
Topics:
'''

# Python Casting
'''
int => float
'''
intval = 6
floatval = float(intval) # 6.0
strval = str(intval) # '6'
print(floatval)
print(strval)
print('Type of intval: ',type(intval), 'Type of strval: ',type(strval))
# strig value me agar koi bhi albhabet hai to usko hum int ya float me convert nahi kar sakte hain.
name = '87687'
print(int(name))


# Specify a Variable Type
'''
varaible ke andar kis type ki value padi hain uko pata karan.
ye pata karene ke liye type method ka use kiya jata hain
'''

# Python Strings
'''
String normal case me ek theroy likhne ka tarika hain.
'''

# String Literals: str()
name = 'Python'
name1 = "New Python"

# Assign String to a Variable: value ko assign karne ke liye equalto sign ka use karte hain.
print('\n\nName: ',name)


# Multiline Strings
studentDetails = '''
Hello Welcome to python class

No  Name
1   Megha
2   Vikash
'''
print(studentDetails)


# Strings are Arrays
'''
Array:
1D = One Dimetion => Index array
2D = Two Dimethon => Associative Array
3D = Three Diethon => Multidimetion array

Array me indexing values 0 se start hoti hain
'''
name = 'Megha learning python'
print('\n\nName: ',name[4])


# Slicing
print('\n\nSlicing value: ',name[6:12]) # because range hamesa (n-1)

# Negative Indexing
print('\n\nName: ',name[-5:-1])


# String Length
print('\nLength of name: ',len(name))

# String Methods
# strip()
newstr = ' Python Class '
print('\nNewstr: ',newstr, 'Len of newstr: ',len(newstr))
print('\nnewStr with strip method: ',newstr.strip(), 'Len of newstr using strip method: ',len(newstr.strip()))
# lower()
print('\nstr using lower: ',newstr.lower())
# upper()
# replace(): is case me 2 arguments ki jarurat hain
print('\nReplace: ',newstr.replace('P','A'))
print('\nTitle: ',newstr.islower())

# split()
againstr = 'New,Python'
print('\nSplit: ',againstr.split(','))

# Check String
newstr = 'Hello python how are you kaise ho.'
print('\nCheck how is exist or nor: ', 'How' in newstr)

# String Concatenation: +
a = 'Python'
b = 'Course'
print(a + ' ' + b)

# String Format
print('\n Hello Vikash welcome to {} {}'.format(a,b))

# Escape Character
print('\\bHello team\\s')

'''
Excercise:

1. name varaibel me apna name likhna hai aur usko str method ka use karke upper case me output show karan hai.
2. str ke baki methods ko run karke check karna hain.
'''


'''
Questions:

1. learn about array and how many types of array?
2. 
'''