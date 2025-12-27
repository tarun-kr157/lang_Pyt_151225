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

import json
with open("data/MOCK_DATA.json") as f:
    data = json.load(f)
# print(type(data))
# print(data[0]['gender'])
# print()


# for count in data: # in is a memebership operator
#     if count['gender'] == 'Male':
#         print(f"Male: {count['first_name']}")
#     elif count['gender'] == 'Agender':
#         print(f"Agender: {count['first_name']}")
#     elif count['gender'] == 'Bigender':
#         print(f"Bigender: {count['first_name']}")
#     else:
#         print(f"Female: {count['first_name']}")

count = 0
while (count != len(data)):
    gender = data[count]['gender']
    name = data[count]['first_name']
    if gender == 'Male':
        print(f"Male: {name}")
    elif gender == 'Agender':
        print(f"Agender: {name}")
    elif gender == 'Bigender':
        print(f"Bigender: {name}")
    else:
        print(f"Female: {name}")
    count += 1

# print()
# import json
# with open("data/MOCK_DATA.json") as file:
#     data = json.load(file)
#     print(type(data))



    
