# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14

@author: Xiang Li
"""
from data_structures import Stack

def parChecker(symbolString):
    '''
    in: a string containing all symbols
    return: boolean, true for balaced, vice versa
    Completed extended parenthesis checker for: [,{,(,),},]
    '''
    leftPar = Stack()
    strList = list(symbolString)
    balanced = True
    symbol = {'[':']','{':'}','(':')'}
    i = 0
    
    while i < len(symbolString) and balanced:

        if strList[i] in ['[','(','{']:
            leftPar.push(strList[i])
            
        else:
            if leftPar.isEmpty():
                balanced = False
                
            else:
                if not strList[i] == symbol[leftPar.pop()]:
                    balanced = False
        i += 1
    
    if not leftPar.isEmpty():
        balanced = False
    
    
    return balanced

#%% test

print(parChecker('{{([][])}()}'))
print(parChecker('[{()]'))
print(parChecker('[{()}'))
print(parChecker('[{()}]]'))