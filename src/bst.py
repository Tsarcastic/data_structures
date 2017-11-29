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
                        # balance!
                        completed = True
                    else:
                        cur = cur.right

                elif new_node.key < cur.key:
                    if not cur.left:
                        cur.left = new_node
                        completed = True
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

    def balancing(self, parent, child):
        """Adjust balance for the tree."""
        while parent.parent:
            if parent.left.key == child.key:
                parent.left_depth += 1
            elif parent.right.key == child.key:
                parent.right_depth += 1

            balance = parent.right_depth - parent.left_depth
            if balance == -2:
                if parent.left and parent.left.left:
                    self.left_left(parent)
                elif parent.left.right:
                    self.left_right(parent)

            elif balance == 2:
                if parent.right and parent.right.right:
                    self.right_right(parent)

    def left_left(self, root):
        """Left-left case - Right rotation."""
        pivot = root.left
        root.parent = pivot
        root.left = None
        pivot.right = root
        pivot.right_depth += 1
        root.left_depth += -2

    def right_right(self, root):
        """Right-right case - Left rotation."""
        pivot = root.right
        pivot.parent = root.parent
        root.parent = pivot
        root.right = None
        pivot.left = root
        pivot.left_depth += 1
        root.right_depth += -2
        if not pivot.parent:
            self.root = pivot

    def left_right(self, root):
        """It's just a jump to the left. And a step to the ri-i-i-ight."""
        right = root
        center = root.left.right
        left = root.left

        if right == self.root:
            self.root = center
        else:
            if right.parent.left == right:
                right.parent.left == center
                right.parent.left_depth += -1
            elif right.parent.right == right:
                right.parent.right == center
                right.parent.right_depth += -1

        left.right = None
        left.parent = center

        center.left = left
        center.parent = right.parent
        center.right = right
