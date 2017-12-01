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
        """Constructor for the BST object."""
        self.root = None
        self.size = 0
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
            completed = False
            while not completed:

                if new_node.key == cur.key:
                    raise Exception("That number is already in the tree.")

                self.size += 1

                if new_node.key > cur.key:
                    if not cur.right:
                        cur.right = new_node
                        new_node.parent = cur
                        self.depth_adjust(new_node)
                        completed = True
                    else:
                        cur = cur.right

                elif new_node.key < cur.key:
                    if not cur.left:
                        cur.left = new_node
                        new_node.parent = cur
                        self.depth_adjust(new_node)
                        completed = True
                    else:
                        cur = cur.left

    def right_rotation(self, root):
        """Left-left case. Right rotation. Bottom remains unchanged."""
        pivot = root.left

        pivot.parent = root.parent
        if not pivot.parent:
            self.root = pivot

        root.left = pivot.right
        root.parent = pivot
        if root.left:
            root.left_depth = max(root.left.left_depth, root.left.right_depth) + 1
        else:
            root.left_depth = 0

        pivot.right = root
        pivot.right_depth = max(root.left_depth, root.right_depth) + 1

    def left_rotation(self, root):
        """Right right case. Left rotation. Bottom remains unchanged."""
        pivot = root.right

        pivot.parent = root.parent
        if not pivot.parent:
            self.root = pivot

        root.right = pivot.left
        root.parent = pivot
        root.right_depth = max(root.right.left_depth, root.right.right_depth) + 1

        pivot.left = root
        pivot.left_depth = max(root.left_depth, root.right_depth) + 1

    def balance(self, node):
        """If a node has a balance of 2 or -2 you flip it and reverse it."""
        return node.right_depth - node.left_depth

    def adjust(self, child):
        """Flip it and reverse it."""
        parent = child.parent
        grandparent = parent.parent
        if self.balance(grandparent) == -2:
            if self.balance(parent) == -1:
                self.right_rotation(grandparent)
            else:
                self.left_rotation(parent)
                self.right_rotation(grandparent)

    def depth_adjust(self, child):
        """Adjust the depth when a new child is added."""
        while child.parent.parent:
            if child.parent.right == child:
                child.parent.right_depth = max(child.left_depth, child.right_depth) + 1
            elif child.parent.left == child:
                child.parent.left_depth = max(child.left_depth, child.right_depth) + 1
            if child.parent.parent.right == child.parent:
                child.parent.parent.right_depth = max(child.parent.left_depth, child.parent.right_depth) + 1
            elif child.parent.parent.left == child.parent:
                child.parent.parent.left_depth = max(child.parent.left_depth, child.parent.right_depth) + 1
            self.adjust(child.parent.parent)
            child = child.parent


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
        """Receive a node and return its replacement descendent."""
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

        else:
            if cur.left:
                tracker = cur.left

                if not tracker.left:
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
                    raise ValueError('The BST does not contain that')
                if cur.right.value == value:
                    cur.right = self.restructure(cur.right)
                    completed = True
                else:
                    cur = cur.right


