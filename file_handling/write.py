'''
File handling me open method with a argumetn:

1. Agar file pahle se exist karta hai to usi file me last se jo bhi data hai usko add kardega. Jisko ki hum append kahte hai. Aur yahi same work list me append method karta hai.
2. Agar file exist nahi karta hai to hame error nahi milega, balki new file crete ho jayega.

File Handling me open method me 'w' argument:

1. Ye agar file exits nahi karta hai to use create karega but error nahi dega.
2. But agar file exist karta hai to usem new data to old data se replase kar dega.

'a' : if not exists then create a new file. append data on file
'w' : create file if not existsa and also overwrite the data on this file
'''

fileWrite = open("c:/xampp/htdocs/htmldemo/learn-python-code-basic-to-advance-with-videos/file_handling/demo.txt","a")

name = input('Enter your name: ')
course = input('Enter your course: ')

userData = '''

Hello, {0}
How are you {0}, you are learing {1}

'''.format(name,course)

fileWrite.write(userData)
fileWrite.close()

# w argument in file
fileWriteWithW = open("c:/xampp/htdocs/htmldemo/learn-python-code-basic-to-advance-with-videos/file_handling/userdata.txt","w")
# name = input('Enter your name: ')
# course = input('Enter your course: ')

userData = '''
Hello, {0}
How are you {0}, you are learing {1}

'''.format(name,course)

fileWriteWithW.write(userData)
fileWriteWithW.close()