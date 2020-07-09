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


