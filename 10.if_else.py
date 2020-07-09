# अगर डेवलपमेंट फील्ड मे आना चाहते हो और समझ नहीं आ रहा है की कैसे क्या करू को तो मुझे कान्टैक्ट कर सकते हो heykyakaru@gmail.com पर और मैं कोसिस करूंगा सही गाइड करने की। क्योंकी बिना सही गाइड के कई बार हम काफी परेसान हो जाते हैं की क्या करे और कैसे करे और इससी चक्कर मे काफी समय और पैसे की बर्बादी कर देते हैं। इसके बाद काफी मानसिक तनाव का भी सामना करना पड़ता हैं तो इसी परेसानी को कम करने का छोटा सा प्रयास हैं। 

# साथ ही अपने ज्ञान को आपके साथ बांटने के लिए यूट्यूब चैनल शुरू किया हूँ और आपके साहियोग की जरूरत है इसे सही और जरूरत मंद स्टूडेंट्स और जो खुद से पढ़ पढ़ना चाहते हैं उन तक पहुचाने के लिए तो इस चैनल को उनके साथ जरूर शेयर करो जो वाकई मे पढ़ना चाहते है और खुद से कोसिस कर रहे हैं। 
# https://www.youtube.com/channel/UCphs2JfmIClR62wbyf76HDg

# HEY KYA KARU यूट्यूब चैनल के जरूरी लिंक 
# 1. Python Basic and Advance ट्यूटोरियल प्लेलिस्ट https://www.youtube.com/playlist?list=PLK6wiPavf7QikS9PMYrGZXz1HlE1KZLD3
# 2. PHP Projects प्लेलिस्ट https://www.youtube.com/playlist?list=PLK6wiPavf7QiEj6IPc3lkjz1wR4w9RM6B
# 3. GitHubट्यूटोरियल प्लेलिस्ट  https://www.youtube.com/watch?v=LUyVs2MTlTM&list=PLK6wiPavf7Qjydpc5v-hdIoqCx2V19pHP
# 4. Python Project https://www.youtube.com/watch?v=3lrbbB38zpU&list=PLK6wiPavf7Qj-NLJhbkxw9QfonweHafcN
# 5. Tips and Trick for Development: https://www.youtube.com/watch?v=vPL6ODrfcwI&list=PLK6wiPavf7QiVLYXrC2TW_fdcZp57MgMB


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
