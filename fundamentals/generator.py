
eggs = (x*2 for x in [1, 2, 3, 4, 5])
#
# for i in eggs:
#     print i
#


def gen():
    yield 1
    yield 2
    yield 3

myGen = gen()
print myGen.next()
print myGen.next()
print myGen.next()
# print myGen.next()