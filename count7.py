# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 20:32:48 2015

@author: Shawn Li
"""

def count7(N):
    ''' Find the occurance of 7 in a given digit
    Args:
        N: a non-negative integer
    Return:
        N: integer
    '''
    if N > 0:
        if (N % 10) == 7:
            return 1 + count7(N // 10)
        else: 
            return count7(N // 10)
    else:
        return 0
        
#%% Test the fuction
count7(1247857)