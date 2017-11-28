"""Binary Search Tree: Basic Edition."""

from que_ import Queue


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
        self.list = []
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

    def in_order(self, node):
        """Return values in order traversal."""
        if node:
            self.in_order(node.left)
            self.list.append(node.value)
            self.in_order(node.right)
        return self.list

    def pre_order(self, node):
        """Return values pre order."""
        if node:
            self.list.append(node.value)
            self.pre_order(node.left)
            self.pre_order(node.right)
        return self.list

    def post_order(self, node):
        """Return values post order."""
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            self.list.append(node.value)
        return self.list

    def breadth_first(self):
        """Return values breadth first."""
        q = Queue()
        q.enqueue(self.root)
        while len(q) > 0:
            node = q.dequeue()
            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)
            self.list.append(node.value)
        return self.list

    def io_generator(self, node):
        """Return values in order traversal."""
        if node:
            self.in_order(node.left)
            yield node.value
            self.in_order(node.right)

    def delete(self, value):
        """Delete a node with the given value, or return no-op."""
        if self.root.value == value:
            if not self.left and not self.right:
                self.root = None
            else:
                # Restructuring
                pass
        cur = self.root
        completed = False
        while not completed:
            if value < cur.value:
                if cur.left.value == value:
                    # Restructuring
                    pass
                else:
                    cur = cur.left
            else:
                if cur.right.value == value:
                    # Restructuring
                    pass
                else:
                    cur = cur.right
   
   def restructure(self, cur, side):
        """Restructure."""
        if side == 'left':
            if not cur.left.left and not cur.left.right:
                # No children
                cur.left = None
            elif cur.left.left and cur.left.right:
                peepaw = cur.left.right
                
                if not peepaw.left:
                    peepaw.left = cur.left.left
                    cur.left = peepaw
                
                while peepaw.left.left:
                    peepaw = peepaw.left
                
                replacement = peepaw.left 
                peepaw.left = replacement.right
                replacement.left = cur.left.left 
                replacement.right = cur.left.right
                cur.left = replacement

            else:
                if cur.left.left:
                    replacement = cur.left.left
                    while replacement.right:
                        replacement = replacement.right


            elif cur.left.left and cur.left.right:
                # Two children
                replacement = cur.left.right
                if not replacement.left:
                    # If Replacement doesn't have a left node Replacement keeps its right and left is reassigned.
                    replacement.left = cur.left.left
                    cur.left = replacement
                while replacement.left:
                # Moves to the left
                    replacement = replacement.left
                if replacement.right:
                    cur.left.right.left = replacement.right
                cur.left.right.left = replacement.right
                replacement.left = cur.left.left
                replacement.right = cur.left.right
                cur.left = replacement