# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13

@author: Xiang Li


"""

class Stack:
    '''
    use attributes of List to define data structures stack
    '''

    def __init__(self):
        self.items = []
    
    def __str__(self):
        return str(self.items)
        
    def pop(self):
        return self.items.pop()
    
    def push(self,item):
        return self.items.append(item)
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return self.items == []

'''
if __name__ == '__main__':
    print('ok')
    a = Stack()
    a.push('a')
    print(a)
    a.push('b')
    print(a)
    print(a.peek())
    print(a.size())
    print(a.isEmpty())
    print(a.pop())
'''