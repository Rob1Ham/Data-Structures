from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        #limit of number of cache entries that can be held
        self.limit = limit
        #the cache is blank at first, so length 0
        #this will keep track of the number of nodes being held
        self.length = 0
        #using DLL as the storage structure of the cache
        #it will hold the key-value entries in correct order
        self.storage = DoublyLinkedList()
        #library starts as a blank dictionary
        self.library = dict()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        #need to check if the key is in the library
        if key in self.library:
            #if the key is in the dictionary
            #set the node as the values related
            #to that key
            node = self.library[key]
            #move the called noded to the end
            self.storage.move_to_end(node)

            return node.value[1]
        else:
            #key not found, return none
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        #checking for special case
        #of the key already existing in the cache
        if key in self.library:
            #if already in the cache
            #set the node as the previous entry
            node = self.library[key]
            #assign the key value pair in the node
            #this is important if the value is new but
            #key is the same
            node.value = (key, value)
            #since it was called most recently
            #it is moved to the top of the stack
            self.storage.move_to_end(node)
            return
        #if the cache is full
        if self.length == self.limit:
            #drop the oldest value in the cache (head)
            del self.library[self.storage.head.value[0]]
            #remove the cache entry for the oldest entry
            self.storage.remove_from_head()
            #reduce length by one
            self.length -= 1
        
        #with the old entry dropped
        #add new entry
        #the tail is the newest entry in the cache
        self.storage.add_to_tail((key, value))
        #the library dictionary needs the updated reference
        #pointing to the newest value in the cache assigned above
        self.library[key] = self.storage.tail
        #cache gets increased length
        self.length += 1