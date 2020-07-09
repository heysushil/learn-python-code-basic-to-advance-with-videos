# अगर डेवलपमेंट फील्ड मे आना चाहते हो और समझ नहीं आ रहा है की कैसे क्या करू को तो मुझे कान्टैक्ट कर सकते हो heykyakaru@gmail.com पर और मैं कोसिस करूंगा सही गाइड करने की। क्योंकी बिना सही गाइड के कई बार हम काफी परेसान हो जाते हैं की क्या करे और कैसे करे और इससी चक्कर मे काफी समय और पैसे की बर्बादी कर देते हैं। इसके बाद काफी मानसिक तनाव का भी सामना करना पड़ता हैं तो इसी परेसानी को कम करने का छोटा सा प्रयास हैं। 

# साथ ही अपने ज्ञान को आपके साथ बांटने के लिए यूट्यूब चैनल शुरू किया हूँ और आपके साहियोग की जरूरत है इसे सही और जरूरत मंद स्टूडेंट्स और जो खुद से पढ़ पढ़ना चाहते हैं उन तक पहुचाने के लिए तो इस चैनल को उनके साथ जरूर शेयर करो जो वाकई मे पढ़ना चाहते है और खुद से कोसिस कर रहे हैं। 
# https://www.youtube.com/channel/UCphs2JfmIClR62wbyf76HDg

# HEY KYA KARU यूट्यूब चैनल के जरूरी लिंक 
# 1. Python Basic and Advance ट्यूटोरियल प्लेलिस्ट https://www.youtube.com/playlist?list=PLK6wiPavf7QikS9PMYrGZXz1HlE1KZLD3
# 2. PHP Projects प्लेलिस्ट https://www.youtube.com/playlist?list=PLK6wiPavf7QiEj6IPc3lkjz1wR4w9RM6B
# 3. GitHubट्यूटोरियल प्लेलिस्ट  https://www.youtube.com/watch?v=LUyVs2MTlTM&list=PLK6wiPavf7Qjydpc5v-hdIoqCx2V19pHP
# 4. Python Project https://www.youtube.com/watch?v=3lrbbB38zpU&list=PLK6wiPavf7Qj-NLJhbkxw9QfonweHafcN
# 5. Tips and Trick for Development: https://www.youtube.com/watch?v=vPL6ODrfcwI&list=PLK6wiPavf7QiVLYXrC2TW_fdcZp57MgMB


# list
# index []
x = 746473
listval = [1,2,3,4,5,6]
print(type(listval))
# list ki indexing wo 0 se start hoti
print(listval[0])

listval = ['hello','7637',8383738,'python',['hello','7637',8383738,'python']]
print(listval[4])
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
print(listval.append)

'''
add value
add list
list ke end me value add hoti hai

clear se puri lest clear ho rahi

'''

listval.clear()

del listval

'''
Question:

'''

'''
Excersice:

1. program banao jisme user se input le ke usko ek list me add karna hai aur final uska output show karana hai. is lise me kewal minimum 5 user ke name input kar ke unko show karna hai.

2. jo user list banaya hai usme se agar user kisi index position ki value ko delet karna chata hai to user input se index possition le ke use vaue ko list se delte karke final list ka output show karana hai.

3. current list ka use karke agar user koi name enter karta hai aur wo exist karta hai to wo name show karna hai other wise ek name not fount ka messaage show karna hai?

4. current list me user ye pata karna chata hai ki koi name kitni baar exist kar raha hai. agar user ne jo name enter kiya hai wo ek baar se jada bar hai to message show karna hai ki wo name total kitni bar hai list me otherwise normal message show karna hai ki name kewal ek baar hi list me exist karta hai.

5. current list ka use karke user ko koi name search karna hai aur agar wo name list me hai to user ko wo name delete karna hai.

6. current list me mohan, sohan, ram, syam ko add karna hai aur inko finally assending order me sort karke output show karan hai. iske liye uper code me dekh lena ki sorting kaise ki gai hai.
'''

