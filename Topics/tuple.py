a = ()
b = 1, 2, 3
c = (4, 5, 6, True, 4.2, "Hello", 3+4j, {}, {10}, [1,2,3])
enames = ('Alice', "Bob", "Charlie", "Modi", "RG")
print(a)
print(b)
print(c)
print(enames)
print(type(c[9]))
# enames[2] = "David" # This will raise an error because tuples are immutable
for name in enames:
    print(name, end=", ")
print()   

# [1, 2, 3]  list is unhashable/mutable, it can be updated after creation and tuple is hashable/immutable, it cannot be updated after creation

print(1 + int("5"))