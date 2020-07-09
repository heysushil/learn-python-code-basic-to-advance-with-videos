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
