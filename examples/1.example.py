'''
Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 100 and 200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''

l = []
for a in range(100, 200):
    if a % 7 == 0 and a % 5 != 0:
        l.append(str(a))

print(','.join(l))
# output = ','.join(l)
# print(type(output))

username = []
print('Enter Your friends name: ')
for i in range(5):
    name = input()
    username.append(name)

print(username)

