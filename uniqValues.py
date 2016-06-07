# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 22:30:02 2015

@author: apple
"""

def uniqueValues(aDict):
    '''return keys that has unique value in a dictionary
    Args:
        aDict: a dictionary
    Return:
        list: a list of keys
    '''
    dictReverse = dict()
    keyValues = list(aDict.items())
    for i in keyValues:
        if i[1] not in dictReverse.keys():
            dictReverse[i[1]] = []
            dictReverse[i[1]].append(i[0])
        else:
            dictReverse[i[1]].append(i[0])
            
    Key = []
    for i in dictReverse.values():
        if len(i) == 1:
            Key.append(i)
    uniqKeys = [y for x in Key for y in x]
    uniqKeys.sort()
    return uniqKeys
    
#%%
#uniqueValues({1: 1, 2: 2, 3: 3})
#uniqueValues({1: 1, 2: 1, 3: 1})
#uniqueValues({1: 1})
uniqueValues({1: 1, 2: 1, 3: 3})
