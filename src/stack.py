"""Creates a stack - a subset of Linked List."""


class Node(object):
    """Creates a node object."""

    def __init__(self, data, next_node):
        """Constructor for the Node object."""
        self.data = data
        self.next = next_node


class Stack(object):
    """Create a stack where things can be stacked on and taken off."""
  
    def __init__(self):
        """Constructor for the Stack object."""
        self.head = None
        self._counter = 0

    def push(self, val):
        """Add a new value to the head of the linked list."""
        new_head = Node(val, self.head)
        self.head = new_head
        self._counter += 1

    def pop(self):
        """Remove & return the value of the head of the Linked List."""
        if not self.head:
            raise IndexError("The list is empty, so there's nothing to pop.")
        output = self.head.data
        self.head = self.head.next
        self._counter -= 1
        return output

    def __len__(self):
        """Work with len() function to find # of items in the stack."""
        return self._counter
