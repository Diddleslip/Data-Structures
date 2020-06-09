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
        self.size = 0
        self.head = None
        self.tail = None

    def __len__(self):
        current = self.head
        count = 0
        while current:
            count +=1 
            current = current.get_next()
        return count

    def push(self, value):
        new_node = Node(value)

        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.size += 1
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

        data = self.tail.get_value()

        if self.head is self.tail:
            self.head = None
            self.head = None
        else:
            self.size -= 1
            current = self.head

            while current.get_next() != self.tail:
                current = current.get_next()

            self.tail = current

        return data

        # if self.size == 0:
        #     return None
        # else: 
        #     self.size -= 1
        #     return self.storage.pop()
