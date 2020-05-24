# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 12:51:32 2020

@author: safal
"""


class Employee:
    raise_amount = 1.05  #Class Variable
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first +'.' + last + '@example.com'
        
                
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def pay_raise(self):
        self.pay = int(self.pay * self.raise_amount) #Employee.raise_amount is also okay
  

class Developer(Employee):
    raise_amount = 1.22
    
    def __init__(self, first, last, pay, pro_lang):
        super().__init__(first, last, pay)
        self.pro_lang = pro_lang
        
class Manager(Employee):
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees
        
        def add_emp(self, emp):
            if emp not in self.employees:
                self.employees.append(emp)
        
        def remove_emp(self, emp):
            if emp in self.employees:
                self.employees.remove(emp)
        
        def print_emps(self):
            for emp in self.employees:
                print('-->', emp.fullname())
            
        
        
        

dev_1 = Developer('Safal','Mahat',40000, 'Python')
dev_2 = Developer('Suraj','Bohora', 45000, 'Java')


mng_1 = Manager('Jack', 'Thapa', 42000, [dev_1])
mng_2 = Manager ('John', 'Cena', 32000, [dev_2])
print(mng_1.email)

mng_1.add_emp(dev_2)
# mng_1.remove_emp(dev_1)
# mng_1.print_emps()

print(mng_1.email)
# print(dev_1.email)
# print(dev_2.pro_lang)

# print(dev_1.pay)
# dev_1.pay_raise()
# print(dev_1.pay)
