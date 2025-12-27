import random
# PART-1 

print(f'The random number is: {random.randint(1, 100)}')
print()
print (f'Random float between 0 & 1: {random.uniform(0, 1):.1f}')
print()
while True:
    num = random.randint(50, 100)
    if num % 2 == 0:
        print(f'Random even numbe between 50 & 100: {num}')
        break
    else:
        continue
print()
for val in range (5):
    print(random.randint(10, 50))
print()
arr = []
for count in range(10):
    arr.append(random.randint(1, 100))
    print(arr[count], end=' ')
print()
print(f'list = {arr}')







 