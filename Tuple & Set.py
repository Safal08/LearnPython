# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 16:17:05 2020

@author: safal
"""

#Tuple
#Lists and tuples are same but one major difference is that lists are mutable and tuples are immutable
#mutable
list_1=['Math','History','Science','Statistic']
list_2=list_1
print(list_1)
print(list_2)

list_1[0]='Art'
print(list_1)
print(list_2)


#immutable
tuple_1=('Math','History','Science','Statistic')
tuple_2=tuple_1
print(tuple_1)
print(tuple_2)

#tuple[0]='Art'
#print(tuple_1)
#print(tuple_2)

#Sets
cs_courses={'Math','Physics','English','DBMS'} #no duplicate and unordered
art_courses={'Math','Design','English','Account'}
print(cs_courses)
print('Math' in cs_courses)
print(cs_courses.intersection(art_courses)) #intersection
print(cs_courses.union(art_courses)) #union
print(cs_courses.difference(art_courses)) #Difference

#empty list
empty_list = []
empty_list = list()

#empty tuple
empty_tuple = ()
empty_tuple = tuple()

#empty set
empty_set = {} # This is incorrect, it creates  dictionary
empty_set = set() #This way is used to create the empty set

#Note
#[] -> list
#() -> tuple
#{} -> set
