a=15
b=0b11111
c=0o17
d=0xA
print(a, b, c, d)
print(id(a), id(b), id(c), id(d))
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# typecatsing  
price=15
print(int(price))
print(bin(price))
print(oct(price))
print(hex(price))
print(float(price))

fruits = ["apple", "banana", "cherry", "banana"]
print(set(fruits))
"""x, y, z = fruits
print(x)
print(y)
print(z)

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)"""