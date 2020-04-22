# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 12:08:05 2020

@author: safal
"""


#function in python
#function supports DRY

def hello_func(): #Declared using the def
    #pass
    print('Hello my first function')
    return 'Hey use of return here'   #use ofreturn in function

hello_func() #calling function
print(hello_func())

#passing parameter in python

def hello_world(greeting):
    return '{} World!'.format(greeting) #passing argument to function in python
print(hello_world('Hello'))

#Adding two number using function
def add(a,b):
    sum1 = a+b
    return sum1

print(add(5,6))

#add string to argument
def hello_universe(x,y):
    return '{} {}'
print('Hello', 'Universe!')

def student_info(*args, **kwargs): # * is for list and ** is for dictionary
    print(args)
    print(kwargs)

courses = ['Math', 'Art']
info ={'name':'Jack', 'age':21}

#student_info(courses,info) -> inappropriate
student_info(*courses,**info) #now this is appropriate way


#Example of whole
month_days=[0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #0 is for placeholder for indexing

def is_leaf(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if not 1 <= month <= 12:
        return 'Invalid month'
    if month == 2 and is_leaf(year):
        return 29
    
    return month_days[month]

print(is_leaf(2020))
print(days_in_month(2020,2))




