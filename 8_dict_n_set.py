'''
Dictionary:

key => value
'''

user = {'name':'Sachin','course':'python'}
print('\n\nuser type: ',type(user))
print('user: ',user['name'])

# get()
print('user by get: ',user.get('name'))

# value change
user['name'] = 'Mr. Sachin'

# add
user['mobile'] = 98838373837

# pop()
user.pop('mobile')

# popitem()
user.popitem()

# del
# del user

# copy()
newuser = user.copy()

newuser['address'] = 'India'
newuser['email'] = 'sachin@gamil.com'

# clear()
user.clear()

# user dict method
againuser = dict(newuser)

# multilevel dict
detial = {
    'sachin' : {
        'course':'python',
        'address':'India'
    },
    'neha': {
        'course': 'New Python',
        'address': 'New India'
    }
}

print('Final user output: ',user)
print('Newuser: ',newuser)
print('againuser: ',againuser)
print('\n\ndetials: ',detial)

# get indiviaal value by key
print('sachin data: ',detial['neha']['course'])

# other methos of dict

'''
Program:

Dict programs

1. ek dictinoary banai hai jisme ki mininum 3 users ke personal details add karne hain aur usme bhi har ek user ke 10th aur 12th couse ko school key ke andar add karna hai aur isko multiline sting ka use karke output show karna hai.

2. ek list bana hai aur uslist me kai minimum 5 friends ko add karna hai aur harek fried personal details dictonary me store karna hai. iske baad multiline string ka use karke output show karna hai jisme ki har ek friend ka alag - alag personal detils show karana hai.
'''

newlist = ['Ram',{}]
