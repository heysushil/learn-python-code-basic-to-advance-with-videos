# pip package manager
'''
1. Module ka use kare rahe hai
2. Python me file create and ukso next python file me import kiya tha.
3. Pre install module = datetime / math / json


Agar hum koi other librarys python me use karna chate hai then:

ABout Pip:

1. ye librarys ka collection
2. ye librarys difrent types hain:
    For example: Scipy, Matplotlib.pyplot, Panda

Pip ka version check karne ke liye terminal me command run karna hain: pip --version    
'''
# for install camelcase run: pip install camelcase
import camelcase as c

name = 'heysushil'
mycamel = c.CamelCase()

print('\nMy name is ',mycamel.hump(name))

# for uninstall camelcase: pip uninstall camelcase

# for geting list of preinstalled pip pacakes: pip list