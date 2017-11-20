"""."""


def test_bst_root():
    """."""
    from bst import BST
    import pytest
    b = BST()
    b.insert(9)
    assert b.root.value == 9


def test_bst_1layer():
    """."""
    from bst import BST
    import pytest
    b = BST()
    b.insert(9)
    b.insert(10)
    assert b.root.right.value == 10


def test_contains01():
    """."""
    from bst import BST
    import pytest
    b = BST()
    b.insert(9)
    b.insert(10)
    assert b.contains(10)


def test_depth01():
    """."""
    from bst import BST
    import pytest
    b = BST()
    b.insert(9)
    b.insert(10)
    assert b.depth == 1


def test_balance01():
    """."""
    from bst import BST
    import pytest
    b = BST()
    b.insert(9)
    b.insert(10)
    assert b.balance == 1