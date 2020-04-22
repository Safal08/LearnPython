# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 09:49:00 2020

@author: safal
"""


num=3
print(type(num)) #shows the integer

num1=3.14
print(type(num1)) #shows the float

#Arithmetic Operations
print(5+2) #Addition
print(5-2) #Subtraction
print(5/2) #Division
print(5//2) #Floor Division
print(5**2) #Exponent
print(5%2) #Modulus

num=num+1 #increment
print(num)
num-=1 #decrement shorthand operator
print(num)
print(abs(-3)) #abs function
print(round(3.23)) #round function
print(round(4.3334,2)) #round with 2 argument

#comparisons
num_1=3
num_2=4
print(num_1==num_2) #Equal return boolean
print(num_1!=num_2) #Not Equal return boolean
print(num_1>num_2) #Greater than
print(num_1<num_2) #Less Than
print(num_1<=num_2) #Less than equal to
print(num_1>=num_2) #Greater than equal to

a='200'
b='300'
a=int(a) #casting
b=int(b) #casting
print(a+b)