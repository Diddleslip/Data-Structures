"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next_node = next

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class Queue:
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

    def enqueue(self, value):
        new_node = Node(value)

        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

        # self.size += 1
        # return self.storage.append(value)

    def dequeue(self):
        if self.head is None:
            return None

        data = self.head.get_value()

        current = self.head

        self.head = current.get_next()

        return data


        # if self.size == 0:
        #     return None
        # else:
        #     self.size -= 1
        #     return self.storage.pop(0)
