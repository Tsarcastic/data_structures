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
        self.dict_of_words = {}

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
            self.dict_of_words[string] = True
            self.size += 1

    def contains(self, string):
        """Will return True if the string is in the trie, False if not."""
        if string is isinstance(string, str):
            raise TypeError('Word is not a string')
        if string is'':
            return False
        return string in self.dict_of_words

    def _size(self):
        """Will return the total number of words in the trie. 0 if empty."""
        return self.size

    def remove(self, string):
        """Will remove the given string from the trie."""
        if string is '':
            return False
        if string is isinstance(string, str):
            raise ValueError('You have to type a string.')
        current_node = self.root
        # while not finished: