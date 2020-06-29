listval = [1,2,3,4,10]
print(all(listval))

a = [1,2,3]
b = a
c = list(a)
# d = c
print(a == b)
print(a == c)
print(a is c)
print(type(a),type(c))
print(id(a),id(b),id(c))
# print(a is d)

listval = [1,2,3,4,5]
listval.append(10)
listval.insert(2,20)

print(listval)

print(format(77878,"b"))


char = []
for i in range(50,70):
    # char.append(chr(i))
    print(chr(i))

print(char)

print(dir())


print(list(reversed(listval)))

a = [1,2,3]
b = ['one','two','three']
print(list(zip(a,b)))
print(dict(zip(a,b)))