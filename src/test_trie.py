"""Test that trie tree."""

import pytest


@pytest.fixture
def basic_setup():
    """A basic setup."""
    from trie import Trie
    t = Trie()
    return t


def test_basic(basic_setup):
    """Add a banana."""
    basic_setup.insert('Banana')
    assert 'B' in basic_setup.root.next_node


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

deft test_cant