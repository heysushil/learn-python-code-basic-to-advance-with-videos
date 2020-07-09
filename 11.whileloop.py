# अगर डेवलपमेंट फील्ड मे आना चाहते हो और समझ नहीं आ रहा है की कैसे क्या करू को तो मुझे कान्टैक्ट कर सकते हो heykyakaru@gmail.com पर और मैं कोसिस करूंगा सही गाइड करने की। क्योंकी बिना सही गाइड के कई बार हम काफी परेसान हो जाते हैं की क्या करे और कैसे करे और इससी चक्कर मे काफी समय और पैसे की बर्बादी कर देते हैं। इसके बाद काफी मानसिक तनाव का भी सामना करना पड़ता हैं तो इसी परेसानी को कम करने का छोटा सा प्रयास हैं। 

# साथ ही अपने ज्ञान को आपके साथ बांटने के लिए यूट्यूब चैनल शुरू किया हूँ और आपके साहियोग की जरूरत है इसे सही और जरूरत मंद स्टूडेंट्स और जो खुद से पढ़ पढ़ना चाहते हैं उन तक पहुचाने के लिए तो इस चैनल को उनके साथ जरूर शेयर करो जो वाकई मे पढ़ना चाहते है और खुद से कोसिस कर रहे हैं। 
# https://www.youtube.com/channel/UCphs2JfmIClR62wbyf76HDg

# HEY KYA KARU यूट्यूब चैनल के जरूरी लिंक 
# 1. Python Basic and Advance ट्यूटोरियल प्लेलिस्ट https://www.youtube.com/playlist?list=PLK6wiPavf7QikS9PMYrGZXz1HlE1KZLD3
# 2. PHP Projects प्लेलिस्ट https://www.youtube.com/playlist?list=PLK6wiPavf7QiEj6IPc3lkjz1wR4w9RM6B
# 3. GitHubट्यूटोरियल प्लेलिस्ट  https://www.youtube.com/watch?v=LUyVs2MTlTM&list=PLK6wiPavf7Qjydpc5v-hdIoqCx2V19pHP
# 4. Python Project https://www.youtube.com/watch?v=3lrbbB38zpU&list=PLK6wiPavf7Qj-NLJhbkxw9QfonweHafcN
# 5. Tips and Trick for Development: https://www.youtube.com/watch?v=vPL6ODrfcwI&list=PLK6wiPavf7QiVLYXrC2TW_fdcZp57MgMB


# loop: while / for

if 10 > 15:
    print('this is if conditon')
else:
    print('all condtions are worng')    

'''
do{
    do body
}while(condtion);


In codntion only runs if or else dependns on thier contions

In loop if we use else then doesn't matter loop is running or not but else away show it's massage


While: in while we use condion

For: but in for loop be are useing identity operator to perform iteration
'''

'''
intilization
while condtion:
    body of while
    increment/decremnt
'''

print('\n')
a = 1
while a <= 10:
    print(a)
    a += 1
# using else to get the message
else:
    print('end of whille loop')


# break
user = ['ram','syam','seeta','geeta']
a = 0
u = len(user)
# print(u)
# exit()
while a < u:
    print(user[a])
    if 'syam' in user:
        print('\nWe found syam')
        break
    a += 1

# continue: it use to skip the value which we found
while a < 10:
    a += 1
    # print(user[a])
    if a == 5:
        print('\nWe found syam')
        continue
    print(a)


# tuple
