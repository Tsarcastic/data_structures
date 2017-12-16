"""Create a Queue consisting of Nodes."""


class Node(object):
    """A Node which contains a value."""

    def __init__(self, data, previous, priority=99):
        """Create a new Node. Lower priority is better."""
        self.data = data
        self.previous = previous
        self.next_node = None
        self.priority = priority


class Priority_Q(object):
    """A Line of Nodes."""

    def __init__(self):
        """Create an empty queue."""
        self.head = None
        self.tail = None
        self._counter = 0

    def insert(self, val, priority=99):
        """Add a node to the tail of the queue."""
        new_tail = Node(val, self.tail, priority)
        if self.tail is None:
            self.head = new_tail
            self.tail = new_tail
        else:
            self.tail.next_node = new_tail
            self.tail = new_tail
        self._counter += 1

    def pop(self):
        """Remove a node from the head of the queue."""
        if not self.head:
            raise IndexError("There is nothing to dequeue.")
        output = self.head
        curr = self.head
        while curr:
            if curr.priority < output.priority:
                output = curr
            curr = curr.next_node
        if output.next_node and output.previous:
            output.next_node.previous = output.previous
            output.previous.next_node = output.next_node
            self._counter -= 1
        elif self._counter is 1:
            self.head = None
            self.tail = None
            self._counter -= 1
        else:
            self.tail = self.tail.previous
            self.tail.next = None
            self._counter -= 1
        return output.data

    def peek(self):
        """Access the value of the head of the queue."""
        return self.head.data

    def size(self):
        """Return the size of the queue."""
        return self._counter

    def __len__(self):
        """Work with len() function to find length of linked list."""
        return self._counter
