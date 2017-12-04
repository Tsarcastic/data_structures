"""Test that trie tree."""

import pytest


def test_basic():
    """Add a banana."""
    from trie import Trie
    t = Trie()
    t.insert('Banana')
    assert'B' in t.root.next_node


def test_contains_true():
    """Contain a banana."""
    from trie import Trie
    t = Trie()
    t.insert('Banana')
    assert t.contains('Banana')


def test_contains_false():
    """Contain a banana, not an apple."""
    from trie import Trie
    t = Trie()
    t.insert('Banana')
    assert not t.contains('Apple')

def test_contains_partial_false():
    """Does not contain a ban."""
    from trie import Trie
    t = Trie()
    t.insert('Banana')
    assert not t.contains('ban')

def test_DOES_contain_ban():
    from trie import Trie
    t = Trie()
    t.insert('Banana')
    t.insert('ban')
    assert t.contains('ban')