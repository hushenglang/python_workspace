# list: readable and writable
list = [1, '2', 'three']
print list
for item in list:
    print item
print 1 in list

print '######'

# tuple: only readable
tuple = (3, '4', 'six')
print tuple
for item in tuple:
    print item
print 4 in tuple

print '######'

# sets: there are 2 ways to define the set using set()function or {xx} curly braces
set = set('bccdddfa')
print set
for item in set:
    print item
newset = {33, 4, 3, 2, 2, 2, 1, 1, 4, 3, 2, 3, 2}
print newset
for item in newset:
    print item

#dic
dic = {'name': 'hushenglang', 'gender': 'male'}
print dic['name']

