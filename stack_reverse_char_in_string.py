# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13

@author: Xiang Li

IDE: Spyder Python 3.4
"""
from data_structures import Stack

def revstring(mystr):
    """
    :type mystr: string
    :rtype: string
    use Stack Last In First Out feature to reverse a string
    """
    aStack = Stack()
    
    for i in list(mystr):
        aStack.push(i)
        
    revstr = ''
    
    while not aStack.isEmpty():
        revstr += aStack.pop()
    
    return revstr
    
#%%test
print(revstring('apple'))
print(revstring('x'))
print(revstring('1234567890'))
print(revstring('desserts'))
    