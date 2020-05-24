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
    
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount = amount
        
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
        
emp_1 = Employee('Dexter', 'Morgan', 40000)
emp_2 = Employee('Debra', 'Morgan', 35000)


Employee.set_raise_amt(1.09)

print(Employee.raise_amount) #all are same 
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_str_1 = 'Safal-Mahat-70000'
emp_str_2 = "Suraj-Bohora-80000"
emp_str_3 = "Ashim-Pandey-90000"



new_emp_2 = Employee.from_string(emp_str_2)

print(new_emp_2.email)
print(new_emp_2.pay)

import datetime
my_date = datetime.date(2020, 4, 24)

print(Employee.is_workday(my_date))

