# # a program to determine a give number is 3 digit or not
# num = int(input("Enter a number: "))
# if abs(num) >= 100 and abs(num) <= 999:
#     print("3 digit number")
# else:
#     print("Not a 3 digit number")
# # to maintain dummy block, we use pass statement

# # min_max number program
# def min_max(a, b, c):
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     else:
#         return c
# print(min_max(10, 20, 30))

# if "Salman":
#     print("Salman is still bachelor")
# else:
#     print("We don't know")

# enames = ["Rahul", "Tarun", "Ravi", "Modi"]
# eids = (101, 102, 103, 104) # tuple, hashable or immutable
# eids_set = {101, 102, 103, 104} # set, index-based access not possible
# eids_list = [101, 102, 103, 104] # list, index-based access possible
# emp_dict = [{"eid":101, "ename":"Rahul", "gender": "Male", "sal": 75000}, {"eid":102, "ename":"Tarun", "gender": "Male", "sal": 75000}, {"eid":103, "ename":"Ravi", "gender": "Male", "sal": 75000}, {"eid":104, "ename":"Modi", "gender": "Male", "sal": 75000}] # dictionary

# for i in enames:
#     print(i)
# print()
# for j in eids:
#     print(j)
# print()
# for k in eids_set:
#     print(k)
# print()
# for l in emp_dict:
#     print(l)
# print()
# for emp in emp_dict:
#     print(emp['ename'])
# print()
