"""Binary Search Tree: Basic Edition."""


class Node(object):
    """Creates a node object."""

    def __init__(self, key, value=None, left=None, right=None):
        """Constructor for the Node object."""
        self.key = key
        if not value:
            self.value = key
        else:
            self.value = value
        self.left = left
        self.right = right


class BST(object):
    """Class for the binary search tree."""

    def __init__(self, iterable=()):
        """Constructor for the Linked List object."""
        self.root = None
        self.size = 0
        self.depth = 0
        self.right_depth = 0
        self.left_depth = 0
        self.balance = 0
        if hasattr(iterable, '__iter__') or isinstance(iterable, str):
            for item in iterable:
                self.insert(item)

    def insert(self, key, value=None):
        """Insert a new node into the binary search tree."""
        new_node = Node(key, value)
        if not self.root:
            self.root = new_node
        else:
            cur = self.root
            depth_tracker = 0
            completed = False
            while not completed:
                if self.contains(new_node.value):
                    raise Exception("That number is already in the tree.")
                if new_node.key > cur.key:
                    depth_tracker += 1
                    if not cur.right:
                        cur.right = new_node
                        completed = True
                        self.depth_side(new_node.value, depth_tracker)
                    else:
                        cur = cur.right
                elif new_node.key < cur.key:
                    depth_tracker += 1
                    if not cur.left:
                        cur.left = new_node
                        completed = True
                        self.depth_side(new_node.value, depth_tracker)
                    else:
                        cur = cur.left

    def contains(self, val):
        """Test if a tree contains a certain value."""
        cur = self.root
        while True:
            if cur.value == val:
                return True
            elif val < cur.value:
                if cur.left:
                    cur = cur.left
                else:
                    return False
            elif val > cur.value:
                if cur.right:
                    cur = cur.right
                else:
                    return False

    def depth_side(self, val, depth):
        """Adjust depth & balance."""
        if val > self.root.value:
            self.right_depth = max(self.right_depth, depth)
            self.depth = max(self.right_depth, self.left_depth)
            self.balance = self.right_depth - self.left_depth
        else:
            self.left_depth = max(self.left_depth, depth)
            self.depth = max(self.right_depth, self.left_depth)
            self.balance = self.right_depth - self.left_depth
