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
        self.parent = None
        self.left_depth = 0
        self.right_depth = 0


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
                        cur.right_depth += 1
                        completed = True
                        self.depth_side(new_node.value, depth_tracker)
                    else:
                        cur.right_depth += 1
                        cur = cur.right

                elif new_node.key < cur.key:
                    depth_tracker += 1
                    if not cur.left:
                        cur.left = new_node
                        cur.left_depth += 1
                        completed = True
                        self.depth_side(new_node.value, depth_tracker)
                    else:
                        cur.left_depth += 1
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

    def restructure(self, cur):
        """Restructure."""
        if not cur.left and not cur.right:
                return None
        elif cur.left and cur.right:
            tracker = cur.right

            if not tracker.left:
                tracker.left = cur.left
                return tracker

            else:
                while tracker.left.left:
                    tracker = tracker.left

                replacement = tracker.left
                tracker.left = replacement.right
                replacement.left = cur.left
                replacement.right = cur.right
                return replacement
                # Yassss

        else:
            if cur.left:
                tracker = cur.left

                if not tracker.right:
                    return tracker

                else:
                    while tracker.right.right:
                        tracker = tracker.right

                    replacement = tracker.right
                    tracker.right = replacement.left
                    replacement.left = cur.left
                    return replacement

            else:
                tracker = cur.right

                if not tracker.left:
                    return tracker

                else:
                    while tracker.left.left:
                        tracker = tracker.left

                    replacement = tracker.left
                    tracker.left = replacement.right
                    replacement.right = cur.right
                    return replacement

    def delete(self, value):
        """Delete a node with the given value, or return no-op."""
        if self.root.value == value:
            self.root = self.restructure(self.root)
            return
        cur = self.root
        completed = False
        while not completed:
            if not cur.value:
                return ValueError('The BST does not contain that value')

            elif value < cur.value:
                if not cur.left:
                    raise ValueError('The BST does not contain that value')
                elif cur.left.value == value:
                    cur.left = self.restructure(cur.left)
                    completed = True
                else:
                    cur = cur.left

            else:
                if not cur.right:
                    raise ValueError('The BST does not contain that value')
                if cur.right.value == value:
                    cur.right = self.restructure(cur.right)
                    completed = True
                else:
                    cur = cur.right
