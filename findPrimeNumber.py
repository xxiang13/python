# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 16:01:27 2015

@author: Shawn Li
IDE: Spyder python 3.4
math reference: http://www.wikihow.com/Check-if-a-Number-Is-Prime
"""
import math

def primesList(N):
    ''' Find prime numbers in range 2 to N (N included)
    Args:
        N: an integer
    Return:
        list: list of prime numbers
    '''
    # Your code here
    toCheck = range(3,N+1)
    primes = [2]
    for i in toCheck:
        a = 0
        find = False
        while not find and primes[a] <= math.sqrt(i):
            if i % primes[a] == 0:
                find = True
            else:
                a += 1
        if not find:
            primes.append(i)
                
    return primes  
    
#%% Test the function
primesList(20)