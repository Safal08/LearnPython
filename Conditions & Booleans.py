# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 18:25:54 2020

@author: safal
"""


#Conditionals and Booleans
#No switch is in python
#if, elif, else keyword is used in conditional

language = 'Java'
if language=='Python':
    print('Language is Python')
elif language=='Java':
    print('Language is Java')
else:
    print('No match')
    
num1 = 14
num2 = 17

if num1 < num2:
    print("Num1 is smaller than num2")
else:
    print("Num1 is greater than num2")
    
#Boolean and, or, not

user='Admin'
logged_in = True
if user=='Admin' and logged_in==True:
    print('Admin page')
else:
    print('Error')
#is
a=[1,2,3,4]
b=[1,2,3,4]
print(id(a))
print(id(b))

print(a is b) #is is same as print(id(a)==id(b))

#false values in condition
#False
#None
#Zero of any numeric type
#Any empty sequencr (), [],''
#Any empty mapping {}

#example

condition = True

if condition:
    print('True Evaluation')
else:
    print("False Evaluation")
