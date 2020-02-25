import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        #DLL is good for a queue because adding and removing elements from the head/tail is O(1)
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        #adding to the queue means adding to the tail
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        #queues remove from the head
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_head()

    def len(self):
        return self.size