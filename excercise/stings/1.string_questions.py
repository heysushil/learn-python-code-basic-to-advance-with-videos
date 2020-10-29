'''
Python String Excercise Questions with Hey Sushil:

1. Kisis bhi stirng ki kitni length hai ye kaise pata kare?

2. Ek string me har char kitni bar aaya hai kaise pata karenge?
Sample String : google.com
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

3. Kisi bhi string mese use first 2 aur last 2 char show karn hai but agar string len 2 hai then isko double time show karna hai but agar char 1 hai then kuch nahi show karna hai?

Sample String : 'heySushil'
Expected Result : 'heil'
Sample String : 'he'
Expected Result : 'hehe'
Sample String : ' 'h'
Expected Result : Empty String

4. Ek string me jaha bhi s hai usko $ me change kardo?
Sample String : 'heysushil'
Expected Result : 'hey$u$hil'

5. 2 alag-alag stirng ko ek karna hai aur sath hi dono str ke first char apas me swap karne hai?
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'

6. Input word ke last me 'ing' add karn hai lekin 'ing' agar pahle se hai then 'ly' add karna hai 'ing' hata kar lekin agar word 3 char se chota hai then waise hi show kardo?
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'strly'

7. Input string me agar not aur poor hain then unko good se replace kardo lekin agar koi ek hi word hai poor ya not me se then waise hi show kardo?
Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!'

8. Ek function bano jo word ko list me store kare aur jiski length sab se jada ho usko batao.

9. Koi bhi length ki input string me se last char ko kaise remove karenge?

10. Kaise kisi bhi string me first aur last char ko apash me exchange karenge?
'''


# 1. Kisis bhi stirng ki kitni length hai ye kaise pata kare?
mystring = 'Hello Hey Sushil how are you? Badhiya aap kaise hain?'
# mystring = input('\nEnter your message: ')

print('\nFind len of mystirng: ', len(mystring))

if len(mystring) == 0:
    print('\nApp bina koi entry kiye ender kar diye hain?')

# 2. Ek string me har char kitni bar aaya hai kaise pata karenge?
count_mystring_char = {
    'H': mystring.count('H'),
    'e': mystring.count('e'),
}
print('\ncount_mystring_char: ', count_mystring_char)

# string char count funciton
def count_char_of_string(mystring):
    # empty dictinonary for adding keys and values
    dict = {}
    # for loop to get individual char from mystirng
    for s in mystring:
        # get keys for dict
        keys = dict.keys()
        # condtion to get char
        if s in keys:
            dict[s] += 1
        else:
            dict[s] = 1
    # show result
    print('\nFinal result of char count: \n', dict)

mystring = 'Hello Hey Sushil how are you? Badhiya aap kaise hain?'
# call function
count_char_of_string(mystring)

# 3. Kisi bhi string mese use first 2 aur last 2 char show karn hai but agar string len 2 hai then isko double time show karna hai but agar char 1 hai then kuch nahi show karna hai?

name = 'HeySushil'

if len(name) >= 2:
    print('\nName: ', name[0] + name[1] + name[-2] + name[-1])

# 4. Ek string me jaha bhi s hai usko $ me change kardo?
name = 'HeySushil'
newname = name.replace('S','$')
# newname = name.replace('s','$')
print('\ns2$: ', newname)

# 5. 2 alag-alag stirng ko ek karna hai aur sath hi dono str ke first char apas me swap karne hai? abc = xbc | xyz = ayz

name1 = 'abc'
name2 = 'xyz'

newname1 = name2[0] + name1[1:]
newname2 = name1[0] + name2[1:]
print('\nnewname1: ', newname1 + ' ' + newname2)


# 6. Input word ke last me 'ing' add karn hai lekin 'ing' agar pahle se hai then 'ly' add karna hai 'ing' hata kar lekin agar word 3 char se chota hai then waise hi show kardo?
def in_string_add_ing_or_ly(name):
    namelen = len(name)

    if namelen > 3:
        if name[-3:] == 'ing':
            # yaha par kaise ing ko replace kiye jaye ly se
            name += 'ly'
        else:
            name += 'ing'

    print('\nName: ', name)

name = "String"
in_string_add_ing_or_ly(name)

# 7. Input string me agar not aur poor hain then unko good se replace kardo lekin agar koi ek hi word hai poor ya not me se then waise hi show kardo?

# 8. Ek function bano jo word ko list me store kare aur jiski length sab se jada ho usko batao.

def find_len_of_stirng(mystrings):
    newstring = []

    for n in mystrings:
        newstring.append((len(n), n))
    newstring.sort()
    
    print('\nFinal result of long stirng: ', newstring[-1][1])

mystrings = ['heysushil', 'hey', 'you']
find_len_of_stirng(mystrings)


# 10. Kaise kisi bhi string me first aur last char ko apash me exchange karenge?

name = 'heysushil'
print('\nFirs char: ', name[0], ' Last char: ', name[-1])
# name[0] = 'i'
# name[-1] = name[0]
print('\n', name[-1] + name[1:-1] + name[0])