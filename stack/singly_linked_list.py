class Node():
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next

  def set_next(self, new_next):
    self.next = new_next

class LinkedList():
  def __init__(self):
    self.head = None
    self.tail = None

  def add_to_tail(self, data):
    new_node = Node(data)
    if self.tail == None:
      self.tail = new_node
      self.head = new_node
    else:
      self.tail.set_next(new_node)
      self.tail = new_node

  def contains(self, value):
    node = self.head
    while node:
      if node.value == value:
        return True
      node = node.get_next()
    return False

  def remove_head(self):
    if self.head is None:
      return None
    
    val = self.head.get_value()

    if self.head is self.tail:
      self.head = None
      self.tail = None
    else:
      self.head = self.head.get_next()

    return val

  def get_max(self):
    if self.head is None:
      return None
    
    max = self.head.get_value()
    next = self.head.get_next()
    while next:
      if next.get_value() > max:
        max = next.get_value()
      next = next.get_next()
      
    return max

