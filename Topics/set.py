s = set()
#order not preserved, duplicates not allowed, mutable, hetrogeneous data types allowed
s1 = {10}
s2 = {} #this is dictionary not set
print(type(s1))
print(type(s2))
print(type(s))
s.add(20)
s.add(30)
s.add('RG')
s.add(40)
s.remove(30)
print(s)
for item in s:
    print(item)
# print(s[0]) # this will raise an error as sets are not subscriptable
s.add(20) #duplicates not allowed
s.add([1,2,3])

