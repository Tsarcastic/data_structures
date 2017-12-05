"""Trie Basic Edition: DLC sold separately."""


class Node(object):
    """Creates a node object."""

    def __init__(self, value=None, next_node=None):
        """Constructor for the Node object."""
        self.value = value
        self.next_node = {}
        self.entire_word = ""


class Trie(object):
    """Get that Trie, son."""

    def __init__(self):
        """Construct the trie, all smooth-like."""
        self.size = 0
        self.root = Node()

    def insert(self, string):
        """Will insert a string into the trie. Duplicates will be ignored."""
        current_node = self.root
        string.split()
        i = 0
        while i < len(string):
            letter = string[i]
            if letter in current_node.next_node:
                i += 1
                current_node = current_node.next_node(letter)
            else:
                current_node.next_node[letter] = Node(letter)
                current_node = current_node.next_node[letter]
                i += 1
        if not current_node.entire_word:
            current_node.entire_word = string
            self.size += 1


    def contains(self, string):
        """Will return True if the string is in the trie, False if not."""
        if string is'':
            return False
        if string is None:
            raise ValueError('You have to type something in you dingus.')
        current_node = self.root
        string.split()
        i = 0
        while i < len(string):
            letter = string[i]
            if letter in current_node.next_node:
                current_node = current_node.next_node[letter]
                i += 1
            else:
                return False
        if current_node.entire_word == string:
            return True
        else:
            return False

    def _size(self):
        """Will return the total number of words in the trie. 0 if empty."""
        return self.size

    def remove(self, string):
        """Will remove the given string from the trie."""
        if string is '':
            return False
        if string is None:
            raise ValueError('You have to type something in you dingus.')
        current_node = self.root
        while not finished:

