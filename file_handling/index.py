'''
File handling:

File ko handle karne ka matlab hai ki:

1. ya to hum new file create kare
2. existing file me change kare
3. existing file ko delte kare

open() method ka use kare hum ksisi bhi file ko load karte hain.
Is method ka use kane ke liye number of argumets ka use kiya jata hai:

'r' : file read if file not exists show error
'a' : open file as appending aur create a new file if file not exists
'w' : write in file, if file not exists then creat a file
'x' : it's create specific type of file and show error if file not exists

2 other arguemts:
't' : default open text mode
'b' : It's use for Image or multi media data
'''

file = open("c:/xampp/htdocs/htmldemo/learn-python-code-basic-to-advance-with-videos/file_handling/demo.txt","r")
# file ko chekc karne ke liye ki file successfully load hua ya nahi
print('\n', file)

# file ko read karna
# print('\n',file.read())

# file me se specific char get karne ke liye
# print('\n',file.read(10))

# file me se number of line raed karne ke liye
def readFileLines():
    print('\n',file.readline())
    print('\n',file.readline())
    print('\n',file.readline())

# get number by user
# number = int(input('Enter number of lines: '))

readFileLines()

print('\nFile datatype: ',type(file))

# use for loop to get all file data line by line
for f in file:
    print('Lines: ',f)

file.close()
