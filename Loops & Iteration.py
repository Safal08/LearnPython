# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 11:29:03 2020

@author: safal
"""


#Loops and Iteration with use of break and continue

nums = [1, 2, 3, 4, 5]

for num in nums:  #for Loop
    print(num, '\n')



nums1=[2, 6, 8, 10]

for i in nums1:
    if i == 8:
        print('8 is Found!!')
        #break break the loop and doesn't print the next values after 8 is found
        continue #Ignore 8 and print the rest values
    print(i)
    
#nested loop

num_1 = [1,2,3,4,5]
for i in num_1:
    for j in 'abc':
        print(i, j)
print('\n')
        
#example of range function
for k in range(10):
    print(k)
print('\n')
    
#while loop in python
x=0
while x<10:  #use of while loop in python
    print(x)
    x+=1
    
