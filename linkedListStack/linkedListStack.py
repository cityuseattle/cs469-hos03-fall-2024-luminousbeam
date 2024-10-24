class Node:
  # To create nodes for Linked List

  def __init__(self, data):
    # Constructor to initialize the node automatically
    self.data = data
    self.next = None

class LinkedListStack:
  def __init__(self):
    # Set the head pointer for the stack. Default is null
    self.head = None

  def is_empty(self):
    # Check if the stack is empty
    return True if self.head == None else False

  def push(self, data):
    # Add data to the start of the stack
    if self.head == None:
      self.head = Node(data)
    else:
      new_node = Node(data)
      new_node.next = self.head
      self.head = new_node

  def pop(self):
    # Remove the element that is the current head (start of the stack)
    if self.is_empty():
      return None
    else:
      popped_node = self.head
      self.head = self.head.next
      popped_node.next = None
      return popped_node.data

  def peek(self):
    # Get the head node data
    return self.head.data if not self.is_empty() else None

  def print_stack(self):
    # Print the stack's elements
    if self.is_empty():
      print("Stack underflow")
      return

    cur = self.head
    while cur is not None:
      print(cur.data, "->", end=" ")
      cur = cur.next