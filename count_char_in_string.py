# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 11:07:37 2015

@author: Shawn Li
IDE: Spyder Python 3.4
"""

def countVowels(s):
    '''Find number of vowels in a string
    Args:
        String
    Return:
        Integer: number of vowels        
    '''
    vowelDict = {'a':0, 'e':0, 'i':0,'o':0,'u':0}
    char = list(s)
    
    for i in char:
        if i in vowelDict.keys():
            vowelDict[i] = vowelDict[i] + 1
    
    numVowel = sum(vowelDict.values())
    
    return numVowel
    
#%%Test countVowels
s = 'azcbobobegghakl'

countVowels(s)

#%%
def countBob(s):
    '''Find number of 'bob' in a string
    Args:
        String: s
    Returns:
        Integer: number of freq
    '''
    numBob = 0
    for i in range(len(s)):
        if len(s[i:]) >= 3:
            if s[i:i+3] == 'bob':
                numBob += 1
    return numBob
#%%Test countBob
                
s = "azcbobobegghakl"

countBob(s)


        
            