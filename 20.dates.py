# date
'''
Date firstly system date ko fetch karta hai
'''

# import datetime libarary
import datetime as dt

# get current time
getCurrentDateTime = dt.datetime.now()
print('\ngetCurrentDateTime: ', getCurrentDateTime)

print('\nGet year only: ',getCurrentDateTime.year)
print('\nGet year only: ',getCurrentDateTime.strftime('%A'))


'''
%a: get short day name
%A: get full day name
%w: get week day like 2
%d: get day by digit
%b: get month sort form
%B: get full month name
%m: get month digit number
%y: get shor year digit 20,19
%Y: get full version of year
%H: get hourse 24 version
%I: get hourse 12 version
%p: get am or pm
%M: get minut
%S: get second
%f: get microsecond
%z: get timezone UTC offset: Aisa/Kolkata +05:30 
%Z: get Timezone
%j: get total days of one year
%U: get toal weeks on year, by first day as sunday
%W: get total weeks on year by first day as Monday
%c: get local version of date time
%x: get only local verson of date
%X: get local verson of time
'''

d = dt.datetime.now()
print('\nDate: ',d.strftime('%x'))
print('\nTime: ',d.strftime('%X'))

print('\nDate: ',d.strftime('%d'),'/',d.strftime('%m'),'/',d.strftime('%Y'))
