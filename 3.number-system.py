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
Topics:

Python Numbers:
    int: har ek positve and negative number
    float: decimal point number folat hote hain
    complex: j se complex number ko denote kiya jata hai
'''

x = 787
y = '787' # stirng 
# type()
print('\nX: ',type(x))
print('Y: ',type(y))

if(x == y):
    print('\n Yes x == y')
else:
    print('No x not = y')


# float
x = 6.6
print('\nX float type: ',type(x))

# complex
z = 6j
print('\nTYpe of z: ',type(z))

# Type Conversion
# hum int ko float me ya fir in number dataypes ko ek dusre ke the conver kar sakte hain
a = 6
b = float(a)
print('\nB type: ',type(b), 'Value of b: ', b)
c = int(b)
print('C ka type: ',type(c), 'Value of C: ',c)
# int ya float ko complex number me conver kiya ja sakta hain
# lekin comple ko int ya folat me convert nahi kiya ja sakta hain
print('Type of a as complex convert : ',type(complex(a)), 'Value of comple: ',complex(a))
e = 6j
# print('\nComple to int: ',int(e))


# Random Number
# random python me pre installed aata hai.
import random

print('Random number: ',random.randrange(1000, 9999))


'''
Number System:
1. binary (base 2)
2. octal (base 8)
3. decimal (base 10)
4. hexadecimal (base 16)
'''
print('\n\nBinary to decimal: ',0b0111011000)
print('\nOctal to Decimal: ',0o546546450)
print('\nHexa to Decimal: ',0x86878ADF)

# Python Decimal
import decimal
# normal decilmal number
print('\nNormal decimal: ', 0.1)
# using decimal library
print('\nUsing Decimal: ',decimal.Decimal(0.1))
# decimal libary use karne ka resion
'''
jab hame finacial result nikalna ho to decimal lib sahi hai
jab kabhi bhi actual decimal points cahiye tab bhi iska use kar
'''

# Python Mathematics
import math
# har ek library ke andar jo methods hai wo specific number of arguments accept karte hain.
print('\nPi: ',math.pi)
print('Cos of pi: ',math.cos(math.pi))
print('Exp of 10: ',math.exp(10))
# print(math.)

'''
Excersices:

1. conver int flat and complex varable me valus ko store karke and direct prine me convertion ka output bhi show karna hai.
2. math lib ka use karke uske kuch ek method ko print karna hai
3. math lib ke pi value ko decimal lib ke Decimal method me use kar ke chek karna hai.
'''

'''
Questions:
1. random library ko padhna hai aur is ke kuch aur method ka work dekhna hain
2. random, decimal and math lib ke baare me padhna hai
'''