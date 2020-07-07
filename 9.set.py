# set: set unindex form values

a = {3,4,5,6,7,8,97,7}
b = {4,4,3,3,32,3,4,5,6}

print('a: ',a)

# add()
a.add(8787)
print('a.add(8787): ',a)

# update()
a.update([37737,3434,3434])
print('a: ',a)

# len()
print('len: ',len(a))

# remove
# a.remove(37737)
# a.remove(37737)

a.discard(37737)
a.discard(37737)

# pop()
a.pop()

# clear
a.clear()

# del

print('final a: ',a)

print('\nb: ',b)
c = {34,343,4,5,5,4,5,484}
print('c: ',c)


uniq = b.union(c)
print('uniq: ',uniq)

common = b.intersection(c)
print('common: ',common)

diff = b.difference(c)
print('diff: ',diff)

b.intersection_update(c)
print('inter update: ',b)

b.difference_update(c)
print('diffupdate: ',b)

print('isdis: ',c.isdisjoint(b))

print('c.issubset(b): ',c.issubset(b))
b = {3,4,5,6,9}
c = {3,4,5,6,9,4,4555,6677,55}
print('c.issuperset(b): ',c.issuperset(b))


