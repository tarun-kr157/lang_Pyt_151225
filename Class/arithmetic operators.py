a = "Rahul"
b = "20"
c = 10
d = True # boolean type gets converted to 1 when arithmetic operated with int
e = "40, "
f = 30.5
h = False # boolean type gets converted to 0 when operated arithmetic with int
print(a + b)
print(c + d)
print(c*e) # string multiplication, repetition occurs of the string when multiplied with int type data
print(c*f)
print(c+f)
print(f-c)
print(f/d)
print(f%d)
print(f**c)
print(c+h)
print(c-h)
esal = int(input("Enter salary:"))
print(esal >= 40000)
if esal >= 40000:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

for i in range(6):
    print("*" * i)
    print()
for i in range(5, 0, -1):
    print("*" * i)
    print()

for i in range(1, 6):
    print("*" * i)
print()
for j in range(5):
    for k in range(j+1):
        print("*", end="")
    print()
for i in range(10):
    print("*" * i)
for j in range(10, 0, -1):
    print("*" * j)
print()

