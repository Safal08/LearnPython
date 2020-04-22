# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 17:23:49 2020

@author: safal
"""
#Import module and exploring the standard library
import random #importing random from standard library
import datetime
import calendar
import math
import os

#import my_module as mm
from my_module import find_index , test
courses = ['Math', 'Art', 'History']

index=find_index(courses,'History')
#index = mm.find_index(courses, 'Art')
print(index)
print(test)

random_course = random.choice(courses) 
print(random_course)

print(os.getcwd())


