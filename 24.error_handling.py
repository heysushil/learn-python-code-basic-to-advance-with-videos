'''
Error handling:

try: 
except:
finally:
else:
'''
print(name)

try:
    # name = '\nheysushil'
    print(name)
except NameError:
    print('\nNameError successfully handled by me.')    
except TypeError:
    print('\nTypeError handerld')
except:
    print('Sorry name is not found')
# else:
#     print('\n Noting wrong happend')    
finally:
    print('\nFInally our error work is completed.')
    # close()

# direct without try or except ke error handling
num = -1
name = ""
name = 'heysushil'
if not type(name) is int:
    # raise Exception('We are only allow int values.')
    raise TypeError('We are only allow int values.')


'''
1. try aur expect error ko handle karne ke liye hai
2. else ka use tab hota hai jab kisi bhi except care ki jarurt nahi hoti hai ya koi bhi excetp casae run nahi hota hai
3. finally ye hamesa exicute hoga hi hoga. dosn't matter ki try excet ya else me se kya chala.
'''