"""."""

import pytest


@pytest.fixture
def basic_setup():
    """A basic setup with two numbers."""
    from bst_experimental import BST
    b = BST()
    b.insert(9)
    b.insert(10)
    return b


@pytest.fixture
def fancy_setup():
    """A more complicated setup."""
    from bst_experimental import BST
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
    from bst_experimental import BST
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
    from bst_experimental import BST
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


def test_contains01(basic_setup):
    """10 is in the tree."""
    assert basic_setup.contains(10)


def test_depth01(basic_setup):
    """Depth registers correctly."""
    assert basic_setup.depth == 1


def test_balance01(basic_setup):
    """Balance registers correctly."""
    assert basic_setup.balance == 1


def test_contain02(fancy_setup):
    """52 is in the tree."""
    assert fancy_setup.contains(52)


def test_depth02(fancy_setup):
    """Depth is maintained in a fancy setup."""
    assert fancy_setup.depth == 3


def test_depth03(fancy_setup):
    """Left depth registers correctly."""
    assert fancy_setup.left_depth == 3


def test_contains03(fancy_setup):
    """The tree contains 17."""
    assert fancy_setup.contains(17)


def test_right_place_01(fancy_setup):
    """The 52 is where it should be."""
    assert fancy_setup.root.left.left.right.value == 52


def test_balance02(fancy_setup):
    """The correct balance is maintained."""
    assert fancy_setup.balance == -1


def test_duplicate01(fancy_setup):
    """."""
    with pytest.raises(Exception):
        fancy_setup.insert(17)


def test_iterable01():
    """BST will construct from an iterable."""
    from bst import BST
    b = BST([19, 25, 31, 16])
    assert b.root.value == 19


def test_iterable02():
    """Will maintain form."""
    from bst import BST
    b = BST([19, 25, 31, 16])
    assert b.root.right.value == 25


def test_in_order01(fancy_setup):
    """Test in_order method."""
    assert fancy_setup.in_order(fancy_setup.root) == [17, 52, 90, 91, 100, 390, 400]


def test_pre_order01(fancy_setup):
    """Test pre_order method."""
    assert fancy_setup.pre_order(fancy_setup.root) == [100, 90, 17, 52, 91, 400, 390]


def test_post_order01(fancy_setup):
    """Test post_order method."""
    assert fancy_setup.post_order(fancy_setup.root) == [52, 17, 91, 90, 390, 400, 100]


def test_breadth_first(fancy_setup):
    """Test breadth first."""
    assert fancy_setup.breadth_first() == [100, 90, 400, 17, 91, 390, 52]


def test_restructure01(fancy_setup):
    """Test the restructure method on fancy_setup tree."""
    assert (fancy_setup.restructure(fancy_setup.root.right)).value == 390


def test_restructure02(fancy_setup):
    """Test the restructure method on fancy_setup tree."""
    assert (fancy_setup.restructure(fancy_setup.root.left)).value == 91


def test_restructure03(fancy_setup):
    """Test the restructure method on fancy_setup tree."""
    assert (fancy_setup.restructure(fancy_setup.root)).value == 390


def test_delete01(basic_setup):
    """Test those deleteses."""
    basic_setup.delete(9)
    basic_setup.delete(10)
    assert not basic_setup.root


def test_delete02(fancy_setup):
    """Test more deleteses."""
    fancy_setup.delete(100)
    assert fancy_setup.root.value == 390


def test_delete03(fancy_setup):
    """Test more deleteses."""
    fancy_setup.delete(100)
    fancy_setup.delete(390)
    fancy_setup.delete(400)
    assert fancy_setup.root.value == 91


def test_deletenull(fancy_setup):
    """Test more deleteses."""
    with pytest.raises(ValueError):
        fancy_setup.delete(11)


def test_fancier_restructure(fancier_setup):
    """To make sure everything is being built correctly."""
    assert fancier_setup.root.right.left.right.left.value == 180


def test_restructure04(fancier_setup):
    """Test the restructure method on fancy_setup tree."""
    assert (fancier_setup.restructure(fancier_setup.root.right)).value == 175


def test_restructure05(fancier_setup):
    """Test the restructure method on fancy_setup tree."""
    fancier_setup.delete(200)
    assert (fancier_setup.restructure(fancier_setup.root.right)).value == 180


def test_restructure06(fanciest_setup):
    """Test the restructure method on fancy_setup tree."""
    assert (fanciest_setup.restructure(fanciest_setup.root)).value == 150


def test_restructure07(fanciest_setup):
    """Test the restructure method on fancy_setup tree."""
    assert (fanciest_setup.restructure(fanciest_setup.root.left.left)).value == 60


def test_restructure08(fanciest_setup):
    """Test the restructure method on fancy_setup tree."""
    fanciest_setup.delete(53)
    assert fanciest_setup.root.left.left.value == 60