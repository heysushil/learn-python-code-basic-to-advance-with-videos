# python iterators

'''
__iter__(): iter() 
__next__(): next()
'''

newlist = ['car','bike','cicycle']
# fist time iter fucntion 0 index ki value itervalue me store karega.
itervalue = iter(newlist)

# next ko use karke hum 0 index value ko print karegenge
print(next(itervalue))
print(next(itervalue))
print(next(itervalue))
# print(next(itervalue))



# use __iter__() and __next__()
class IterNumber:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 4:
            b = self.a
            self.a += 1
            return b
        else:
            raise StopIteration

# creat objet for print values
iterobj = IterNumber()
classiter = iter(iterobj)

print(next(classiter))
print(next(classiter))
print(next(classiter))
print(next(classiter))
# print(next(classiter))

print('\n\n')
class NewIterClass:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 5:
            b = self.a
            self.a += 1
            return b
        else:
            raise StopIteration

newiterObj = NewIterClass()
# iter ko use karna hai because yahi class se one by one values ko fetch karega
myvar = iter(newiterObj)

for num in myvar:
    print(num)



