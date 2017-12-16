"""Autocomplete using a trie."""
from trie import Node
from trie import Trie

class Autocomplete(object):
    """Autocompletes words."""

    def __init__(self, vocab, max_completions=5):
        """Construct the trie, all smooth-like."""
        self.vocab = Trie(vocab)
        self.max_completions = max_completions

    
    def __call__(self, word):
        """Should autocomplete the word."""
        return (self.vocab.traversal(word))[:self.max_completions]