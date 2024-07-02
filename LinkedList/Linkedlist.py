import os 
import sys

'''
LinkedList is collections of Nodes
where each Nodes are linked with next Node and last Node will be null
First Node we can say HEAD
Last Node is tail



A linked list is a linear data structure in which elements, called nodes, are not stored in contiguous memory locations. Instead, each node contains:

Data: The actual value or information stored in the node.
Pointer (or Reference): A reference to the next node in the sequence.
The main types of linked lists are:

Singly Linked List: Each node points to the next node in the list. The last node points to null.
Doubly Linked List: Each node has two pointers, one pointing to the next node and another pointing to the previous node.
Circular Linked List: The last node points back to the first node, forming a circle.
Advantages
Dynamic Size: The list can grow and shrink in size as needed.
Ease of Insertion/Deletion: Adding or removing nodes is simpler compared to an array, especially at the beginning or end of the list.
Disadvantages
Memory Overhead: Extra memory is needed for storing pointers.
No Random Access: Elements must be accessed sequentially, starting from the head of the list, leading to O(n) time complexity for accessing elements by index.
'''

# %%
class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

    
a = Node(2)
b = Node(3)
c = Node(4)

print(a.data , b.data , c.data)
print(id(a) , id(b) , id(c))

a.next = b
b.next = c

print(a.next)
print(b.next)
print(c.next)


#print(int(0x00000156B3347210))
#print(int(0x00000156B3347050))

class Node:

    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    
    
    '''empty linked list'''
    def __init__(self):
        self.head = None
        '''No of Nodes in LL'''
        self.n = 0
    
    
    
    
        '''append method'''
    def append(self,value):

        new_node = Node(value)
        '''if head is empty then new node becomes head'''
        if self.head == None:
            self.head = new_node
            self.n += 1
            return
        
        curr = self.head

        while curr.next != None:
            curr = curr.next

        curr.next = new_node
        self.n += 1
        

    
    
    
    '''print method'''
    def __str__(self):
        curr = self.head

        result = ''
        while curr != None:
            result = result + str(curr.data) + '->'
            curr = curr.next

        return result[:-2]

    
    
    
    '''len Method'''
    def __len__(self):
        return self.n

LL = LinkedList()
print(LL)
LL.append(10)
print(LL)
LL.append(20)
LL.append(40)
print(len(LL))
print(LL)
    



    
