# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 14:04:06 2015

@author: Shawn Li

IDE: Spyder python 3.4
"""

def findAlphabetSub(s):
    '''Find longest alphabet substrings
    Argus:
        String: string with all lower cases
    Return:
        String: substring
    '''
    
    charList = list(s)
    
    alphabetSubMax = []
    i = 0
    
    while i < len(charList):
        alphabetSub = []
        find = False
        
        while not find and i < len(charList):
            if i != len(charList)-1:
                if charList[i] <= charList[i+1]:
                    alphabetSub.append(charList[i])
                    i += 1
                else:
                    find = True
                    alphabetSub.append(charList[i])
            else: 
                alphabetSub.append(charList[i])
                find = True
                
        if len(alphabetSub) > len(alphabetSubMax):
            alphabetSubMax = alphabetSub
        
        i += 1

    return str(''.join(alphabetSubMax))

#%%Test findAlphabetSub
s = 'rlkxqobqnty'

findAlphabetSub(s)