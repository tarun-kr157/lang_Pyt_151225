# group of key-value pairs/properties/mapped values/entries as one entity
# duplicates not allowed for keys, will overwrite previous value
# heterogeneous data types allowed for keys and values
# order not preserved prior to python 3.7, from 3.7 onwards order is preserved
# mutable
# not index-based

"""my_dict = {
    "eid": "101",
    "name": "RG",
    "esalary": 75000,
    "is_manager": True,
}
print(my_dict)
user_info = {
    "username": "rg123",
    "password": "rg@12345",
    "loc": "India",
    "loc": "India",        # duplicate key, will overwrite previous value
    "is_active": True,
     "age": 48
}
del user_info['is_active']  # deleting a key-value pair
print(user_info['username'])
print(user_info['loc'])
user_info['loc'] = "USA"  # updating existing key
user_info['password'] = "new_password@123"
print(user_info['age'])
print(user_info)

new_dict = {
 "name": "Tarun",
 "profession": "Software Engineer",
 "age": 22,
 "age": 27,
 "is_active": True,
}
print(new_dict)
print(new_dict["is_active"])
del new_dict["is_active"]
print(new_dict)"""

"""for i in range(5):
    for j in range(i, 5):
        print("*", end="")"""
"""for i in range(5):
    for j in range(i, 5):
        print("*", end="")
    print()
for i in range(5, 1, -1):
    for j in range(1, i+1):
        print("*", end="")
    print()
for i in range(5, 0, -1):
    print("*" * i)"""

