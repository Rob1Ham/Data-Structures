import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # DLL Is a good choice for a stack because of the time complexity associated with adding
        # and removing from a DLL is O(1).
        self.storage = DoublyLinkedList()

    def push(self, value):
        #adding to the stack adds to tail
        self.storage.add_to_tail(value)
        self.size += 1
        pass

    def pop(self):
        #stacks remove from the tail
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_tail()
        else: 
            return None

    def len(self):
        return self.size
