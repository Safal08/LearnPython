# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 10:58:31 2020

@author: safal
"""

#string/ Working with textual data
print('Hello World') #printing
message = 'Hello Universe'
print(message)

message1=("John's Phone") #Use of 's while printing
print(message1)

message2='John\'s Phone'
print(message2) #Use of ' within '

print(len(message)) #length of string

print(message[0]) #Character at index 0
print(message[0:5]) # print character from index 0-4, not including index 5
#print(message[:5])
#print(message[6:]) Slicing

#String Methods
print(message.lower()) #into lower case
print(message.upper()) #into upper case
print(message.count('l')) #count method, count the character and takes string as argument
print(message.find('world')) #no universe

new_message=message.replace('Universe','City') #replacing one string with another
print(new_message)

#concatenate using + sign
greeting='Hello' 
name='John'
#output =greeting+name
output =greeting+', '+name

print(output)
#concatenate using placeholder
#output1='{}, {}.Welcome!'.format(greeting,name)
output1=f'{greeting}, {name}.Welcome!'
print(output1) #use of fstring

print(dir(message)) #shows the broad overview of the  attribute 
#print(help(str.lower)) help method


