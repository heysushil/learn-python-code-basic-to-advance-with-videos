'''
File handlind me kisi bhi file ko delete karna:

1. File hanlding me file ko ham direct delete nahi kar sakte hain.
2. Iske liye os library ka use kiya jayega.
3. os library python me operating system level ke activity ke liye use kiya jata hai.

Backward slash \
Forward slash /

OS library me ek module milta hai 'path' naam se isme kafi methods hain but hame file exist check karna hai.

Iske liye os.path.exists() method ka use karnge jisse ki system me jo file hum check kar rahe hai wo exits karti hai ya nahi.
'''

import os


# use remove method to remove any file

# print('\n',os.remove('c:/xampp/htdocs/htmldemo/learn-python-code-basic-to-advance-with-videos/file_handling/demo.txt'))

# print('\n','C:\xampp\htdocs\htmldemo\learn-python-code-basic-to-advance-with-videos\file_handling\demo.txt')

# get user input of file name then delte the file
filename = input('Enter file name which you want to delte: ')
# ye file ka full path hai
mypath = 'c:/xampp/htdocs/htmldemo/learn-python-code-basic-to-advance-with-videos/file_handling/'+filename+'.txt'

print('\nCheck is exists: ',os.path.exists(mypath))
if os.path.exists(mypath):
    print('\n',os.remove(mypath))
else:
    print('\nUser your file is not exists in our database.')

