'''
File handing ka use karke Folder ko delete karna:

1. Hamesa yad rahe ki path agar direct de rahe hain to wo galat hai. Aue isko check karne ke liye print me path to rakhe ke run karke check kiya ja sakta hai.
2. Example: open('C:/xampp/htdocs/htmldemo/learn-python-code-basic-to-advance-with-videos/file_handling/delete_folder.py')
'''

import os

# first code

# deletefile = os.rmdir('C:/xampp/htdocs/htmldemo/learn-python-code-basic-to-advance-with-videos/file_handling/demo_folder')

# print('\ndeletefile: ', deletefile)

folderPath = 'C:/xampp/htdocs/htmldemo/learn-python-code-basic-to-advance-with-videos/file_handling/demo_folder'

# second code
if os.path.exists(folderPath):
    os.rmdir(folderPath)
else:
    print('\nFolder not exists.')