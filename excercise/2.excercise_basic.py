'''
Python excercise list 2 with Hey Sushil:

1. Current month ka calender kaise show karenge? calender module
2. Apni date of birth se current date tak kitne din ke hue kaise pata kare?
3. Agar 20, input number se greate hai then difference ka 5 guna show karo otherwise difference?
4. 
'''

import calendar

print(calendar.month(2020,10))

from datetime import date
# f_date = date(1990, 2, 20)
f_date = date(2020, 10, 20)
l_date = date.today()
delta = l_date - f_date
print(delta.days, ' ldate: ', l_date)

