"""class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hi, I am", self.name)


p1 = Person("Alice")
p1.greet()  # calling method using class name"""

class Solution():
    def unique_character(cls):
        unique_chars = set(cls)   
        print("".join(unique_chars))
        

Solution.unique_character("abcabcbb454fhrhbergfe483")


