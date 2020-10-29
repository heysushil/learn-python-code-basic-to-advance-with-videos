'''
Python excercise list 2 with Hey Sushil:

1. Current month ka calender kaise show karenge? calender module
2. Apni date of birth se current date tak kitne din ke hue kaise pata kare?
3. Agar 20, input number se greate hai then difference ka 5 guna show karo otherwise difference?
4. 10 se 100 ya 200 ke bich ki value agar input ho to kaise pata karenge?
5. 3 alag-alag value ka sum karo lekin 3no value same ho to unke sum ka 3 guna karo.
6. input string me agar 'Hey' nahi likha to add karo aur agar likha hai den same string show karna hai.
7. input string ki n number of copy cahiye hai kaise karenge?
8. input number kaise check kare ki odd hai ya even?
9. [1,4,3,2,5,2,5] is list me 5 kitni baar aaya hai count karna hai?
10. input stirng first 3 char ki n copy cahiye hai aur agar str len less then 3 hai then complete string ki n copy chaiye hai?

1. input char vowel hai ya consonant kaise pata kare?
2. input value group (list, tuple) me hai ya nahi kaise pata kare?
3. input number ko list me convert karo aur list me jitne number hai utne time * print karna hai alag-alag line me?
4. list numbers ko concatenate karn hai str me?
5. is list [33,55,44,22,46,76,12,34,66,88,76,55,99,97,53,52,67] me se even number print karne hai lekin 55 number ke bad wali values nahi print karni hain?
6. 
'''


import calendar

print(calendar.month(2020,10))

from datetime import date
# f_date = date(1990, 2, 20)
f_date = date(2020, 10, 20)
l_date = date.today()
delta = l_date - f_date
print(delta.days, ' ldate: ', l_date)

