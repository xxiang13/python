# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14

@author: Xiang Li
"""

from data_structures import Stack

def baseConverter(decNumber,base):
    '''
    decNumber: decimal number
    base: int between 2 and 16
    
    Algorithm for binary conversion can easily be extended to perform the 
    conversion for any base. In computer science it is common to use a number
    of different encodings. The most common of these are binary, octal (base 8)
    , and hexadecimal (base 16).
    '''
    
    baseNumber = ''
    reminders = Stack()
    
    while decNumber > 0:
        reminders.push(decNumber%base)
        decNumber = decNumber//base
    
    while not reminders.isEmpty():
        baseNumber += str(reminders.pop())
    
    return baseNumber

#%% test
print(baseConverter(233,8))
print(baseConverter(25,2))
print(baseConverter(25,16))
            
            
        