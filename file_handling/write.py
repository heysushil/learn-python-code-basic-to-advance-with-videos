'''
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