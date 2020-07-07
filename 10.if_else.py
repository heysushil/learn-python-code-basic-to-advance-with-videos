'''
Condtions:
'''
# equlas: a == b
a = 10
b = 20

if(a == b):
    print('\nYes (a == b): ')
else:
    print('All conditons are wrong')



# not equal: !=
if a == b:
    print('\nyes a == b')
elif a != b:
    print('\nno a not equal to b')
else:
    print('\nall contiondion false')

# less then: <
c = 10
if a == b:
    print('\nyes a == b')
elif a != c:
    print('\nno a not equal to b')
elif a < b:
    print('\nGreat a is less then b')
else:
    print('\nall contiondion false')

# less then equalto: <=
if a == b:
    print('\nyes a == b')
elif a != c:
    print('\nno a not equal to b')
elif a <= c:
    print('\nOhhoh a is eqal to c')
elif a < b:
    print('\nGreat a is less then b')
else:
    print('\nall contiondion false')

# greater then: >
if a == b:
    print('\nyes a == b')
elif a != c:
    print('\nno a not equal to b')
elif b > a:
    print('\nAwesome B is greater then a')
elif a <= c:
    print('\nOhhoh a is eqal to c')
elif a < b:
    print('\nGreat a is less then b')
else:
    print('\nall contiondion false')

# greater then equalto: >=
if a == b:
    print('\nyes a == b')
elif a != c:
    print('\nno a not equal to b')
elif a >= c:
    print('\nNice a is equal to c but not greater then c')
elif b > a:
    print('\nAwesome B is greater then a')
elif a <= c:
    print('\nOhhoh a is eqal to c')
elif a < b:
    print('\nGreat a is less then b')
else:
    print('\nall contiondion false')


# Logical operators:
print('\n\n a = ',a, ' b = ',b,' c = ',c)
# and
if a < b and c != a:
    print('\nif a < b and c == a:')
elif a > b or c != a:
    print('\nelif a < b or c != a:')
elif not(c == a):
    print('\nelif not(c != a):')
else:
    print('\nAll logical conditions false')
# or
# not

# Idenity: is / is not
users = ['sachin','neha','somya']
# print('\nidentity: ','sachin' is users[0])
if users[0] is not 'mr. sachin':
    print('\nYes sachine is present')

# Memebership: in / not in
# print('\nmembership: ', 'sachin' not in users)
if 'neha' in users and 'mr. sachin' in users:
    print('\nYes class started')
elif 'neha' in users and 'somya' in users:
    print('\n Welcome neha and somya')
else:
    print('\nAll wrong membership and logical conditions')

print('\nUsers: ',users)
if 'neha' in users:
    print('\nHi Neha')
    print('\nHow are you?')

# nested if
if 'Neha' in users:
    print('\nYes neha presenet in class')

    # nested if
    if 'somya' in users:
        print('\nGreat Neha and Somya both present')
else:
    print('\nNeha is not present in class')

    if 'sachin' in users:
        print('\nOnly sachin present in class')
