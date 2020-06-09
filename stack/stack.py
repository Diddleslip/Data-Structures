"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next_node = next

    def get_value(self):
        # returns the Node's data
        return self.value

    def get_next(self):
        # returns the thing pointed at by this node's `next` reference
        return self.next_node

    def set_next(self, new_next):
        # sets this Node's `next` reference to `new_next`
        self.next_node = new_next

class Stack:
    def __init__(self):
        # self.size = 0
        self.head = None
        self.tail = None

    def __len__(self):
        current = self.head
        count = 0
        while current:
            count += 1 
            current = current.get_next()
        return count

    def push(self, value):
        new_node = Node(value)

        if not self.head and not self.tail:
            # self.size += 1
            self.head = new_node
            self.tail = new_node
        else:
            # self.size += 1
            self.tail.set_next(new_node)
            self.tail = new_node

        # self.size += 1
        # new_node = Node(value)
        # new_node.set_next(self.head)
        # self.head = new_node
        # return self.head

    def pop(self):
        if self.tail is None:
            return None
        # save the tail Node's data
        data = self.tail.get_value()
        # both head and tail refer to the same Node 
        # there's only one Node in the linked list 
        if self.head is self.tail:
            # set both to be None
            # self.size -= 1
            self.head = None
            self.tail = None
        else:
            # in order to update `self.tail` to point to the
            # the Node _before_ the tail, we need to traverse
            # the whole linked list starting from the head,
            # because we cannot move backwards from any one
            # Node, so we have to start from the beginning
            current = self.head

            # traverse until we get to the Node right 
            # before the tail Node 
            while current.get_next() != self.tail:
                current = current.get_next()

            # `current` is now pointing at the Node right
            # before the tail Node
            print("THIS IS CURRENT", current.get_value())
            # self.size -= 1
            self.tail = current
            current.next_node = None
            # print("SIZE", self.size)
        
        return data

        # if self.size == 0:
        #     return None
        # else: 
            # self.size -= 1
        #     return self.storage.pop()
