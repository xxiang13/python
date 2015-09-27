# -*- coding: utf-8 -*-
"""
@author: Shawn Li
IDE: Spyder python 3.4

"""

def findTopKwords(tuple_list, k):
    """ Finds the top k items in a list of tuples
    
    Args:
        tuple_list (list): list of tuples
        k (int): top kth values in first position of the tuple
    
    Returns:
        list: list of tuples with top k items 
    
    """
    
    #creat dictionary of freq
    wordFreq = dict()
    for i in tuple_list:
        if i[0] in wordFreq.keys():
            wordFreq[i[0]] = wordFreq[i[0]] + 1
        else:
            wordFreq[i[0]] = 1
    
    #converting dictionary into a list
    wordList = []
    for key, value in wordFreq.items():
        temp = (key,value)
        wordList.append(temp)
    #other way: wordList = list(wordFreq.items())
   
    #find top freq and return corresponding words   
    topKwords = []
    for a in range(k):
        max = 0
        for i in range(len(wordList)):
            if wordList[i][1] > max:
                max = wordList[i][1]
                max_index = i
                
        topKwords.append(wordList.pop(max_index)) 
        #wordList.pop(max_index): delete by index and return deleting value

    return topKwords
    
#%% Test the function
import random
test = [(chr(random.randrange(65,91)),random.random()) for i in range(200)]

findTopKwords(test,10)
