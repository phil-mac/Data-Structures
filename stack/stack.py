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

from singly_linked_list import LinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        length = 0
        if self.storage.head is None:
            return length
        length = length + 1
        next = self.storage.head.get_next()
        while next:
            length = length + 1
            next = next.get_next()
        return length

    def push(self, value):
        # add to head of linked list
        prior_head = self.storage.head
        if prior_head is None:
            self.storage.add_to_tail(value)
        else:
            prior_tail = self.storage.tail
            self.storage.add_to_tail(value)
            self.storage.head = self.storage.tail
            self.storage.head.set_next(prior_head)
            self.storage.tail = prior_tail
            self.storage.tail.set_next(None)

    def pop(self):
        return self.storage.remove_head()


# Array-as-storage version

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.insert(0, value)

#     def pop(self):
#         if len(self.storage) == 0:
#             return None
#         return self.storage.pop(0)