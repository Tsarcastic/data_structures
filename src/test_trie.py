"""Test that trie tree."""

import pytest


def test_basic():
    """Add a banana."""
    from trie import Trie
    t = Trie()
    t.insert('Banana')
    assert 'B' in t.root.next_node


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
    """Partial word returns false."""
    from trie import Trie
    t = Trie()
    t.insert('Banana')
    assert not t.contains('ban')


def test_does_contain_ban():
    """Adding a partial word causes true return."""
    from trie import Trie
    t = Trie()
    t.insert('Banana')
    t.insert('ban')
    assert t.contains('ban')


def test_removing_removes_word():
    """Remove will remove words."""
    from trie import Trie
    t = Trie()
    t.insert('Banana')
    t.remove('Banana')
    assert not t.contains('Banana')


def test_inserting_dupes_are_ignored():
    """Banana don't go in twice."""
    from trie import Trie
    t = Trie()
    t.insert('Banana')
    t.insert('Banana')
    assert t.size == 1


def test_dict_updates():
    """The dict of words stays updated."""
    from trie import Trie
    t = Trie()
    t.insert('Apple')
    t.insert('Banana')
    t.insert('Stalin')
    assert 'Stalin' in t.dict_of_words


def test_removing_banana_leaves_ban_intact():
    """Bananananana."""
    from trie import Trie
    t = Trie()
    t.insert('Banana')
    t.insert('Ban')
    assert t.contains('Ban')
    t.remove('Banana')
    assert t.contains('Ban')
    assert 'Ban' in t.dict_of_words
    assert t.size == 1


def test_removal():
    """Remove it."""
    from trie import Trie
    t = Trie()
    t.insert('Banana')
    assert not t.remove('')


def test_traversal01():
    """Come on baby."""
    from trie import Trie
    t = Trie()
    t.insert('Banana')
    assert t.traversal('') == ['Banana']


def test_traversal02():
    """Come on baby."""
    from trie import Trie
    t = Trie()
    t.insert('Banana')
    t.insert('Ban')
    assert t.traversal('Ban') == ['Ban', 'Banana']


def test_traversal03():
    """Come on baby."""
    from trie import Trie
    t = Trie()
    t.insert('Banana')
    t.insert('Ban')
    assert t.traversal('App') == []
    assert t.size == 2


def test_traversal04():
    """Fruit."""
    from trie import Trie
    t = Trie()
    t.insert('Banana')
    t.insert('Apple')
    t.insert('Grapes')
    t.remove('Grapes')
    assert t.traversal('') == ['Banana', 'Apple']
    assert t.size == 2


def test_traversal05():
    """Numbers? Numbers."""
    from trie import Trie
    t = Trie()
    t.insert(1)
    assert t.traversal('') == ['1']


def test_traversal06():
    """Numbers? Numbers."""
    from trie import Trie
    t = Trie()
    t.insert(1)
    t.insert(1111)
    t.remove(1)
    assert t.traversal('') == ['1111']

def test_iterableinit01():
    """Whereupon our hero is an iterable."""
    from trie import Trie
    words = ['ant', 'banana', 'fruit', 'queen']
    t = Trie(words)
    assert t.contains('ant')
    assert t.contains('banana')