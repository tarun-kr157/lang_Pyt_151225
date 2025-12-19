# class Employee():
#     def __init__(self, eid, ename, esal, is_manager):
#         self.eid = eid
#         self.ename = ename.upper()
#         self.esal = esal
#         self.is_manager = is_manager
#     def display(self):
#         print(self.eid, self.ename, self.esal, self.is_manager)

# emp1 = Employee(101, "Rahul", 75000, True)
# emp1.display()
# emp2 = Employee(102, "Tarun", 75000, False)
# emp1.eid = 656
# #this will not update the ename as it is converted to uppercase in the constructor
# emp2.display()

# print(emp1.ename, end = "!")
# print()
# if (emp1.ename == "RAHUL"):
#     print("Manager")
# else:
#     print("Not Manager")
# print()

while True:
    num = int(input("Enter a number: "))
    if num < 1:
        print("Number cannot be smaller than 1!")
        continue
    else:
        for i in range(1, 11):
            print(f"{num} x {i} = {i*num}")
    break  
        
    







