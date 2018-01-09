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

    def balance(self, node):
        """Return the balance of the bst."""
        return (abs(max(self.root.left_depth, self.root.right_depth) - min(self.root.left_depth, self.root.right_depth)))

    def depth(self):
        """Return the depth."""
        return max(self.root.left_depth, self.root.right_depth)

    def insert(self, key, value=None):
        """Insert a new node into the binary search tree."""
        new_node = Node(key, value)
        if not self.root:
            self.root = new_node
            self.size += 1
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
                        self.neo_depth_adjust(new_node)
                        completed = True
                    else:
                        cur = cur.right

                elif new_node.key < cur.key:
                    if not cur.left:
                        cur.left = new_node
                        new_node.parent = cur
                        self.neo_depth_adjust(new_node)
                        completed = True
                    else:
                        cur = cur.left

    def search(self, val):
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

    def balancing(self, parent):
        """Adjust balance for the tree."""
        grand_pappy = parent.parent
        if grand_pappy:
            balance = grand_pappy.right_depth - grand_pappy.left_depth
            parbal = parent.right_depth - parent.left_depth
            if balance == -2:
                if parbal == -1:
                    self.right_rotation(grand_pappy)
                else:
                    self.left_right(grand_pappy)

            elif balance == 2:
                if parbal == 1:
                    self.left_rotation(grand_pappy)
                else:
                    self.right_left(grand_pappy)

    def del_balancing(self, node):
    """Attempt of a balancing equation."""
        if node.left:
            node.left_depth = max(node.left.left_depth, node.left.right_depth) + 1
        else:
            node.left_depth = 0
        if node.right:
            node.right_depth = max(node.right.left_depth, node.right.right_depth) + 1
        else:
            node.right_depth = 0
        bal = node.right_depth - node.left_depth
        if balance == -2:
            if parbal == -1:
                self.right_rotation(grand_pappy)
            else:
                self.left_right(grand_pappy)

        elif balance == 2:
            if parbal == 1:
                self.left_rotation(grand_pappy)
            else:
                self.right_left(grand_pappy)
        self.neo_depth_adjust(node)   

    def new_balance(self, parent):
        """Balancing method using single rotations."""
        grand_pappy = parent.parent
        g_bal = grand_pappy.right_depth - grand_pappy.left_depth
        par_bal = parent.right_depth - parent.left_depth
        if g_bal == -2:
            if par_bal == -1:
                self.right_rotation(grand_pappy)
            else:
                self.left_rotation(parent)
                self.right_rotation(grand_pappy)

        elif g_bal == 2:
            if par_bal == 1:
                self.left_rotation(grand_pappy)
            else:
                self.right_rotation(parent)
                self.right_rotation(grand_pappy)

    def right_rotation(self, root):
        """Left-left case - Right rotation."""
        pivot = root.left
        base = root.parent
        pivot.parent = base
        if pivot.parent is None:
            self.root = pivot
        elif base.left is root:
            base.left = pivot
        elif base.right is root:
            base.right = pivot
        root.left = pivot.right
        if root.left:
            root.left_depth = max(root.left.left_depth, root.left.right_depth) + 1
        else:
            root.left_depth = 0
        pivot.right = root
        pivot.right_depth = max(root.left_depth, root.right_depth) + 1

    def left_rotation(self, root):
        """Right-right case - Left rotation."""
        pivot = root.right
        base = root.parent
        pivot.parent = root.parent
        if pivot.parent is None:
            self.root = pivot
        elif base.left is root:
            base.left = pivot
        elif base.right is root:
            base.right = pivot
        root.parent = pivot
        root.right = pivot.left
        if root.right:
            root.right_depth = max(root.right.left_depth, root.right.right_depth) + 1
        else:
            root.right_depth = 0
        pivot.left = root
        pivot.left_depth = max(root.left_depth, root.right_depth) + 1

    def left_right(self, root):
        """. It's just a jump to the left. And a step to the ri-i-i-ight."""
        right = root
        center = root.left.right
        left = root.left

        if right.parent is None:
            self.root = center
        else:
            if right.parent.left is right:
                right.parent.left = center
                right.parent.left_depth += -1
            elif right.parent.right is right:
                right.parent.right = center
                right.parent.right_depth += -1

        left.left = None
        left.parent = center
        left.right = None
        left.right_depth = 0
        left.left_depth = 0

        center.left = left
        center.parent = right.parent
        center.right = right
        center.right_depth = 1
        center.left_depth = 1

        right.left = None
        right.right = None
        right.parent = center
        right.left_depth = 0
        right.right_depth = 0

    def right_left(self, root):
        """Riiight. Leeefft. Riiight. Leeefftt."""
        left = root
        center = root.right.left
        right = root.right

        if left.parent is None:
            self.root = center
        else:
            if left.parent.left is left:
                left.parent.left = center
                left.parent.left_depth += 1
            elif left.parent.right is left:
                left.parent.right = center
                left.parent.right_depth += 1

        center.left = left
        center.parent = left.parent
        center.right = right
        center.right_depth = 1
        center.left_depth = 1

        left.right = None
        left.parent = center
        left.left = None
        left.right_depth = 0
        left.left_depth = 0

        right.right = None
        right.parent = center
        right.left = None
        right.left_depth = 0
        right.right_depth = 0

    def neo_depth_adjust(self, child):
        """Giving this another go."""
        parent = child.parent
        if child.left:
            child.left_depth = max(child.left.left_depth, child.left.right_depth) + 1
        else:
            child.left_depth = 0
        if child.right:
            child.right_depth = max(child.right.left_depth, child.right.right_depth) + 1
        else:
            child.right_depth = 0
        if parent:
            if parent.left == child:
                parent.left_depth = max(child.left_depth, child.right_depth) + 1
            elif parent.right == child:
                parent.right_depth = max(child.left_depth, child.right_depth) + 1
        while parent.parent:
            grandparent = parent.parent
            if grandparent.left == parent:
                grandparent.left_depth = max(parent.left_depth, parent.right_depth) + 1
            elif grandparent.right == parent:
                grandparent.right_depth = max(parent.left_depth, parent.right_depth) + 1
            self.balancing(parent)
            parent = grandparent

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
                self.neo_depth_adjust(tracker)
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
                    self.neo_depth_adjust(tracker)
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
                    self.neo_depth_adjust(tracker)
                    return replacement

    def delete(self, value):
        """Delete a node with the given value, or return no-op."""
        if self.root.value == value:
            self.root = self.restructure(self.root)
            self.neo_depth_adjust(self.root)
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
                    self.neo_depth_adjust(cur.left)
                    if cur.right:
                        self.balancing(cur.right)
                    completed = True
                else:
                    cur = cur.left

            else:
                if not cur.right:
                    raise ValueError('The BST does not contain that value')
                if cur.right.value == value:
                    cur.right = self.restructure(cur.right)
                    self.neo_depth_adjust(cur.right)
                    if cur.left:
                        self.balancing(cur.left)
                    completed = True
                else:
                    cur = cur.right
