# Create a list of programming languages
languages = ["Java", "C++", "Python", "JavaScript", "Ruby", "Go"]

# Check if "Python" is in the list
if "Python" in languages:
    print("Python is in the list")
else:
    print("Python is not in the list")




# Input a number and check if it's even or odd
# to verify the whether the element is present in the sequence or not
# membership operators are used to verify the whether the element is present in the sequence or not
# in and not in are membership operators
# in operator returns True if the element is present in the sequence
# not in operator returns True if the element is not present in the sequence
# NOTE:dictionary is not a sequence

eid = [101, 102, 103, 104, 105]
names = ("Rahul", "Ravi", "Raj")
sizes = {"S", "M", "L", "XL"}
ename = "Rahul"
b = bytes([10, 20, 30, 40, 255])
ba = bytearray([10, 20, 30, 40, 255])
fz = frozenset({10, 10, 10})
numbers = range(100)
print(101 in eid)
print(107 in eid)
print(107 not in eid)
print("Ravi" in names)
print("Sahil" not in names)
print("XL" in sizes)
print("a" in ename)
print("g" in ename)
print("g" not in ename)
print(10 in b)
print(10 in ba)
print(10 in fz)
print(80 in numbers)
print(100 in numbers)
print(2**3 in numbers)
print(50//4 not in numbers)
