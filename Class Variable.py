# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 12:51:32 2020

@author: safal
"""


class Employee:
    raise_amount = 1.05  #Class Variable
    no_of_employee = 0
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first +'.' + last + '@example.com'
        
        Employee.no_of_employee += 1
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def pay_raise(self):
        self.pay = int(self.pay * self.raise_amount) #Employee.raise_amount is also okay
    
emp_1 = Employee('Dexter', 'Morgan', 40000)
emp_2 = Employee('Debra', 'Morgan', 35000)

print(emp_1.pay)
emp_1.pay_raise()
print(emp_1.pay)

print(Employee.raise_amount) #all are same 
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(emp_1.__dict__) #emp_1 namespace
print(Employee.no_of_employee)