'''
File handling open method with x argument.

x argument working behaviour:

1. Agar koi file pahle se exist karti hai aur hum usko open karna chate hain x arguments se to hame error milega. Ye error 'FileExistsError' hai
2. Agar jis name se file create kar rahe hai wo exsits nahi karta hai to file us name se file create hoga aur wo open bhi jayega.
'''

# handle error
try:
    myfile = open("c:/xampp/htdocs/htmldemo/learn-python-code-basic-to-advance-with-videos/file_handling/onlydata.txt","x")
    print('\n',myfile)
except FileExistsError:
    print('\nYou are using "x" argumetn in open method. Means file alreday exists.')
    