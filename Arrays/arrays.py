import os 
import sys
import ctypes


"""
Creating my own python lists from ctypes which is used to create a C list
"""


class MeraList:

    def __init__(self):
        self.size = 1
        self.n = 0

        '''create a C types ka list from self.size'''
        self.A = self.__make_array(self.size)



    '''insert method'''
    def insert(self,pos,item):
        if self.n == self.size:
            self.__resize(self.size*2)

        for i in range(self.n,pos,-1):
            self.A[i] = self.A[i-1]

        self.A[pos] = item
        self.n += 1


    '''append method'''
    def append(self,item):
        if self.n == self.size:
            self.__resize(self.size*2)

        self.A[self.n] = item
        self.n += 1


    '''pop method'''
    def pop(self):
        if self.n == 0:
            return "Empty List"
        print(self.A[self.n-1])
        self.n =self.n-1

    
    '''work as find'''
    def __getitem__(self,index):
        if 0<= index < self.n:
            return self.A[index]
        else:
            return "IndexError"

    '''deletion of item'''
    def __delitem__(self,pos):
        if 0 <= pos < self.n:
            for i in range(pos,self.n-1):
                self.A[i] = self.A[i+1]
            
            self.n -= 1


    '''clear method'''
    def clear(self):
        self.n = 0
        self.size = 1

    '''find method'''
    def find(self,item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
        return "ValueError - value not in List"
    
    '''remove method'''
    def remove(self,item):
        pos = self.find(item)
        if type(pos) == int:
            self.__delitem__(pos)
        else:
            return pos

    '''resize method'''
    def __resize(self,new_capacity):
        B = self.__make_array(new_capacity)
        self.size = new_capacity
        #copying the content of old array to new
        for i in range(self.n):
            B[i] = self.A[i]
        #reassign
        self.A = B
    
    
    '''Len Method'''
    def __len__(self):
        return self.n
    
    '''Print method'''
    def __str__(self):
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ',' + ' '

        return '[' + result[:-2] + ']'
    

    '''add list'''
    def add(self,arr):
        if self.n == self.size:
            self.__resize(self.size*2)
            
        for i in range(len(arr)):
            self.append(arr[i])

    
    '''count method'''
    def count(self,value):
        c = 0
        for i in range(self.n):
            if self.A[i] == value:
                c += 1
        return c
            

    '''creating a array'''
    def __make_array(self,capacity):
        #refrential arrays
        return (capacity*ctypes.py_object)()
    
L = MeraList()
L.append(10)
L.append(True)
L.append('Hello')
L.append(394)
L.insert(1,22)
L.remove(22)
print(L.find(33))
arr = MeraList()
arr.append(10)
arr.append(10)
print(L.add(arr))
print(L.count(10))
print(L)



#python list
a = [3,21,1]
b = [10,22]
print(a.sort())