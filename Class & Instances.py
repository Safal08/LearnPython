# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 12:09:32 2020

@author: safal
"""


#python object oriented programming
#Classes and Instances

class Employee:
    def __init__(self, first, last, age): #initializing constructor
        self.first = 'John'
        self.last = 'Cena'
        self.age = 39
        self.email = first + '.' + last +'@example.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('John', 'Cena', 40) #Both are unique
emp_2 = Employee('Christ', 'Swagger', 42)
emp_3 = Employee('Dexter','Morgan',44)

# #print(emp_1)
# print(emp_2)

# emp_1.first = 'John'
# emp_1.last = 'Cena'
# emp_1.age = 39

# emp_2.first = 'Jack'
# emp_2.last = 'Swagger'
# emp_2.age = 39

print(emp_1.email)
print(emp_2.email)

print(emp_2.fullname())
print(emp_1.fullname())
print(Employee.fullname(emp_2))
print(Employee.fullname(emp_3))

