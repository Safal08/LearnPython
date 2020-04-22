# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 17:20:37 2020

@author: safal
"""


print('Imported by my_module...')

test = 'Test String'

def find_index(to_search, target):
    for i, value in enumerate(to_search):
        if value == target:
            return i
        
    return -1