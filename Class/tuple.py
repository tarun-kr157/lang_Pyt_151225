a = ()
b = 1, 2, 3
c = (4, 5, 6, True, 4.2, "Hello", 3+4j, {}, {10})
enames = ('Alice', "Bob", "Charlie", "Modi", "RG")
print(a)
print(b)
print(c)
# print(enames[5])
# enames[2] = "David" # This will raise an error because tuples are immutable
for name in enames:
    print(name)


