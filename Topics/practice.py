# mystr = "banana"
# print(next(iter(mystr)))

# mytuple = ("apple", "banana", "cherry")
# myit = iter(mytuple) #iniates the iterator

# # First pass works fine
# for x in myit: #iterates through the iterator
#     print(x)
# print()
# print(x)    
# print()

# mytuple = ("apple", "banana", "cherry")

# for x in mytuple:
#   print(x)

# b = "Hello,World!"
# print(b[2:5]) # string slicing

# b = "Hello, World!"
# print(b[:6]) # white-space is also treated as part of the string
# print(3,"times",6//3,"is",6) 

import math
import cmath

# Calculate the square root of a negative number (which results in a complex number)

z = eval(input("Enter a complex number: "))
x = cmath.sqrt(z).real
y = cmath.sqrt(z).imag
print(f"Positive z root: {x:.3f} + {y} ")
print(cmath.sqrt(-z))  

# Convert a complex number to polar coordinates
r, phi = cmath.polar(1 + 1j)
print(f"r = {r:.3f}, phi = {phi:.3f}") # Output: (1.41421356..., 0.785398...)

n = int(input("Enter number: "))
result = math.sqrt(n)
print(f"Square root is {result:.3f}")






