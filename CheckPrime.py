# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 13:04:28 2020

@author: safal
"""


#check whether number is prime or not

num = 13
count=0

for i in range(1, num+1):
     
    if num % i  == 0 :
        count=count+1

print(count)
    
if count != 2:
        print('Number is not prime')        
else:
            print("Number is prime")
        
        