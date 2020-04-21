# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 10:19:19 2020

@author: safal
"""

#List

courses=["Math","English","Science","Economics"]
print(courses)
print(len(courses))
print(courses[0]) #index 0 list value
print(courses[-1]) #last index value
courses.append('Computer_sci') #append new parameter to list
print(courses)
courses.insert(0,'Statistic') #specific location and need 2 argument
print(courses)
courses_2=['Health','Population']
courses.extend(courses_2) #use of extend instead of append and insert if there is the involvement of next list 
print(courses)
courses.remove('Health') #Remove value from the list
print(courses)
popped=courses.pop() #Remove the last index
print(courses)
print(popped) #Print the removed value

courses.reverse() #Reverse the list
print(courses)

#Ascending Order
courses.sort() #Sort the list
print(courses)
num=[2,9,3,7]
num.sort() #Sort the number
print(num)

#Decending order sorting
courses.sort(reverse=True)
num.sort(reverse=True)
print(courses)
print(num)

#Sorting without altering original one
sorted_courses=sorted(courses)
print(sorted_courses) #Don't Alter the original list

#Other Build in
print(min(num))
print(max(num))
print(sum(num))
print(courses.index('Science'))
print('Math' in courses) #use of in

for index, item in enumerate(courses, start=0):
    print(index,item)

#change list into strings
course_str =','.join(courses) #Change into string
print(course_str)
new_list=course_str.split(',')
print(new_list) #Change into list
