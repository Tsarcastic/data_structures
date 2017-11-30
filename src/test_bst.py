"""."""

import pytest


@pytest.fixture
def basic_setup():
    """A basic setup with two numbers."""
    from bst import BST
    b = BST()
    b.insert(9)
    b.insert(10)
    return b


@pytest.fixture
def fancy_setup():
    """A more complicated setup."""
    from bst import BST
    b = BST()
    b.insert(100)
    b.insert(90)
    b.insert(17)
    b.insert(400)
    b.insert(390)
    b.insert(91)
    b.insert(52)
    return b


@pytest.fixture
def fancier_setup():
    """Ooooh, fancy."""
    from bst import BST
    b = BST()
    b.insert(100)
    b.insert(200)
    b.insert(175)
    b.insert(190)
    b.insert(180)
    return b


@pytest.fixture
def fanciest_setup():
    """Ooooh, fancy."""
    from bst import BST
    b = BST()
    b.insert(100)
    b.insert(70)
    b.insert(80)
    b.insert(53)
    b.insert(60)
    b.insert(200)
    b.insert(150)
    b.insert(300)
    return b


def test_bst_root(basic_setup):
    """9 is in the tree."""
    assert basic_setup.root.value == 9


def test_bst_1layer(basic_setup):
    """10 is the immediate right child of root."""
    assert basic_setup.root.right.value == 10


#def test_iterable01():
    """BST will construct from an iterable."""
    #from bst import BST
    #b = BST([19, 25, 31, 16])
    #assert b.root.value == 25


def test_iterable02():
    """Will maintain form."""
    from bst import BST
    b = BST([19, 25, 31])
    assert b.root.value == 25

def test_left_left():
    """Left left works."""
    from bst import BST
    b = BST([10, 9, 8])
    assert b.root.value == 9
    assert b.root.left_depth == 1
    assert b.root.right_depth == 1

    assert b.root.left.value == 8
    assert b.root.left.left_depth == 0
    assert b.root.left.right_depth == 0

    assert b.root.right.value == 10
    assert b.root.left_depth == 0
    assert b.root.right_depth == 0

#def test_fancier_restructure(fancier_setup):
    """To make sure everything is being built correctly."""
    #assert fancier_setup.root.value == 100


#def test_restructure04(fancier_setup):
    """Test the restructure method on fancy_setup tree."""
    #assert fancier_setup.root.right.value == 100


#def test_restructure05(fancier_setup):
    """Test the restructure method on fancy_setup tree."""
    #fancier_setup.delete(200)
    #assert fancier_setup.root.left.value == 180
