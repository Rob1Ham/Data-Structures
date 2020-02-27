import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #check if new value is less than current node
        if value < self.value:
            #if there is no left child node
            if not self.left:
                #set the new left child as the new value
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        #if the new value is greater than or = to current node
        if value >= self.value:
            #if there is no right child node
            if not self.right:
                #set the new value as the right child value
                self.right = BinarySearchTree(value)
            else:
                #otherwise, go right again
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #if the node's value is our target
        #return true
        if target == self.value:
            return True
        #if the target is smaller than the node
        #go left
        if target < self.value:
            #if there is no value to the left
            #return False
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        #if the target is bigger than the node
        #go right
        if target > self.value:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

        pass

    # Return the maximum value found in the tree
    def get_max(self):
        #if there is no tree...
        if not self:
            return None
        #if there is no right child
        #return current node's value
        if not self.right:
            return self.value
        #otherwise
        #go right
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        #accoring to the spec
        #calling cb on the value of a node
        cb(self.value)

        #now need to go left and right, and call for_each on each node
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)










    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        #if you can go left
        if node.left:
            #go further down the tree
            self.in_order_print(node.left)

        if node.right:
            #if you can go right
            #print your current value of your node
            #then go right
            #(this preserves the sequential order to print before going further down the tree to the right)
            print(node.value)
            self.in_order_print(node.right)
        else:
            #if you are at a leaf
            #print value
            print(node.value)


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):

        #So to print every value in bredth
        #we use as a queue as we call a node
        #we put the child nodes at the back of the queue
        #this enforces calling all nodes of one level before the next level of nodes are called

        q = Queue()
        #enqueue adds a value to the back of the line.
        #to start the function we put the node passed in at the back/front of the queue
        q.enqueue(node)

        #now, while the queue is not empty...
        while q.len() > 0:
            #we take the node at the front of the queue
            #and set it to current node
            current_node = q.dequeue()
            #print its value
            print(current_node.value)
            #if there is a node to the left, add it to the queu
            if current_node.left:
                q.enqueue(current_node.left)
            #same for right
            if current_node.right:
                q.enqueue(current_node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        #create a stack of current nodes to keep track of
        #place the first node onto the stack

        #while stack isn't empty:
           #pop the top node
           #print node
           #add children to stack
           #put right child on first then left to preserve output order
        
        stack = Stack()
        stack.push(node)
        while stack.len() > 0:
            current_node = stack.pop()
            print(current_node.value)

            #Order is more important for DFT
            #so this lends to a stack's property that whatever was added most
            #
            if current_node.left:
                stack.push(current_node.left)
            if current_node.right:
                stack.push(current_node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
