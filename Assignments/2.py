# PART-2
import random, readchar, string

fruits = ['apple', 'banana', 'mango', 'orange', 'papaya', 'watermelon', 'lychee']

while True:
    key = input("\nPress Enter to pick a fruit (or 'S'/'STOP' to exit): ").strip().lower()
    
     # 1. Check for exit condition first
    if key in ['s', 'stop']:
        print("Goodbye!")
        break
    
     # 2. Since we didn't exit, run the program
    print(f"Random fruit: {random.choice(fruits)}")

print()
students = ['Avinash', 'Tarun', 'Rahul', 'Rakesh', 'Modi', 'Ravi', 'Rohit', 'Raj']
selected = []
selected = random.sample(students, k=3)
print(f'Selected for project: {selected}')
print()
   
arr = list(range(1, 11))
random.shuffle(arr)
print(arr)

numbers = list(range(1, 21))
print(random.sample(numbers, k=5)) # return a list of unique elements
print()

colors = ['red', 'blue', 'green', 'yellow', 'black', 'white']
print(random.choice(colors)) # returns a random element from the list
print()

