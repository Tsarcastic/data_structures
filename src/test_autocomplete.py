"""Tests the autocomplete functions."""
import pytest


def test_setup01():
    """Making sure the foundation is solid."""
    from autocomplete import Autocomplete
    words = ['ant', 'banana', 'fruit', 'queen']
    t = Autocomplete(words)
    assert t.vocab.contains('ant')


def test_setup02():
    """Confirming property works.."""
    from autocomplete import Autocomplete
    words = ['ant', 'an', 'antennae', 'anno', 'antagonize']
    t = Autocomplete(words)
    assert t('a') == ['an', 'ant', 'antennae', 'antagonize', 'anno']


def test_assignment_example01():
    """Testing with the example vocabulary."""
    from autocomplete import Autocomplete
    vocabulary = ['fix', 'fax', 'fit', 'fist', 'full', 'finch', 'final', 'finial']
    complete_me = Autocomplete(vocabulary, 4)
    assert complete_me('f') == ['fix', 'fit', 'fist', 'finch']


def test_assignment_example02():
    """Testing with the example vocabulary."""
    from autocomplete import Autocomplete
    vocabulary = ['fix', 'fax', 'fit', 'fist', 'full', 'finch', 'final', 'finial']
    complete_me = Autocomplete(vocabulary, 4)
    assert complete_me('fi') == ['fix', 'fit', 'fist', 'finch']


def test_assignment_example03():
    """Testing with the example vocabulary."""
    from autocomplete import Autocomplete
    vocabulary = ['fix', 'fax', 'fit', 'fist', 'full', 'finch', 'final', 'finial']
    complete_me = Autocomplete(vocabulary, 4)
    assert complete_me('fin') == ['finch', 'final', 'finial']


def test_assignment_example04():
    """Testing with the example vocabulary."""
    from autocomplete import Autocomplete
    vocabulary = ['fix', 'fax', 'fit', 'fist', 'full', 'finch', 'final', 'finial']
    complete_me = Autocomplete(vocabulary, 4)
    assert complete_me('finally') == []
