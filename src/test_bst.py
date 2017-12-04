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


def test_iterable01():
    """BST will construct from an iterable."""
    from bst import BST
    b = BST([19, 25, 31, 16])
    assert b.root.value == 25


def test_iterable02():
    """Will maintain form."""
    from bst import BST
    b = BST([19, 25, 31])
    assert b.root.value == 25


def test_triple_left():
    """Three on the left."""
    from bst import BST
    b = BST()
    b.insert(50)
    b.insert(40)
    b.insert(30)
    assert b.root.value == 40
    assert b.root.left_depth == 1
    assert b.root.right_depth == 1
    assert b.root.left.value == 30
    assert b.root.left.left_depth == 0
    assert b.root.left.right_depth == 0
    assert b.root.right.value == 50
    assert b.root.right.right_depth == 0
    assert b.root.right.left_depth == 0


def test_triple_right(basic_setup):
    """Ensure that right-right works."""
    basic_setup.insert(20)
    assert basic_setup.root.value == 10
    assert basic_setup.root.left_depth == 1
    assert basic_setup.root.right_depth == 1
    assert basic_setup.root.left.value == 9
    assert basic_setup.root.left.left_depth == 0
    assert basic_setup.root.left.right_depth == 0
    assert basic_setup.root.right.value == 20
    assert basic_setup.root.right.right_depth == 0
    assert basic_setup.root.right.left_depth == 0


def test_left_right():
    """Just a jump to the left. And a step to the ri-i-i-ght."""
    from bst import BST
    b = BST()
    b.insert(50)
    b.insert(40)
    b.insert(45)
    assert b.root.value == 45
    assert b.root.left_depth == 1
    assert b.root.right_depth == 1
    assert b.root.left.value == 40
    assert b.root.left.left_depth == 0
    assert b.root.left.right_depth == 0
    assert b.root.right.value == 50
    assert b.root.right.right_depth == 0
    assert b.root.right.left_depth == 0


def test_right_left():
    """Right rotation then left rotation."""
    from bst import BST
    b = BST()
    b.insert(100)
    b.insert(200)
    b.insert(150)
    assert b.root.value == 150
    assert b.root.left_depth == 1
    assert b.root.right_depth == 1
    assert b.root.left.value == 100
    assert b.root.left.left_depth == 0
    assert b.root.left.right_depth == 0
    assert b.root.right.value == 200
    assert b.root.right.right_depth == 0
    assert b.root.right.left_depth == 0


def test_building_to_fancier():
    """Break down fancier and test it along the way."""
    from bst import BST
    b = BST()
    b.insert(100)
    b.insert(200)
    b.insert(175)
    assert b.root.value == 175
    assert b.root.left_depth == 1
    assert b.root.right_depth == 1
    assert b.root.left.value == 100
    assert b.root.left.left_depth == 0
    assert b.root.left.right_depth == 0
    assert b.root.right.value == 200
    assert b.root.right.right_depth == 0
    assert b.root.right.left_depth == 0


def test_building_to_fancier01():
    """Building."""
    from bst import BST
    b = BST()
    b.insert(100)
    b.insert(200)
    b.insert(175)
    b.insert(190)
    assert b.root.value == 175
    assert b.root.left_depth == 1
    assert b.root.right_depth == 2
    assert b.root.left.value == 100
    assert b.root.left.left_depth == 0
    assert b.root.left.right_depth == 0
    assert b.root.right.value == 200
    assert b.root.right.right_depth == 0
    assert b.root.right.left_depth == 1
    assert b.root.right.left.value == 190
    assert b.root.right.left.right_depth == 0
    assert b.root.right.left.left_depth == 0


def test_building_to_fancier03():
    """Building. First major obstacle."""
    from bst_balancing import BST
    b = BST()
    b.insert(100)
    b.insert(200)
    b.insert(175)
    b.insert(190)
    b.insert(180)
    assert b.root.value == 175
    assert b.root.left_depth == 1
    assert b.root.right_depth == 2

    assert b.root.left.value == 100
    assert b.root.left.left_depth == 0
    assert b.root.left.right_depth == 0
    assert b.root.left.parent.value == 175

    assert b.root.right.value == 190
    assert b.root.right.left_depth == 1
    assert b.root.right.right_depth == 1

    assert b.root.right.left.value == 180
    assert b.root.right.left.right_depth == 0
    assert b.root.right.left.left_depth == 0

    assert b.root.right.right.value == 200
    assert b.root.right.right.right_depth == 0
    assert b.root.right.right.left_depth == 0


def test_building_to_fanciest01():
    """Everything works up to inserting 200."""
    from bst import BST
    b = BST()
    b.insert(100)
    b.insert(70)
    b.insert(80)
    b.insert(53)
    b.insert(60)
    b.insert(200)
    assert b.root.value == 80
    assert b.root.left_depth == 2
    assert b.root.right_depth == 2

    assert b.root.left.value == 60
    assert b.root.left.left_depth == 1
    assert b.root.left.right_depth == 1

    assert b.root.left.left.value == 53
    assert b.root.left.left.left_depth == 0
    assert b.root.left.left.right_depth == 0

    assert b.root.left.right.value == 70
    assert b.root.left.right.left_depth == 0
    assert b.root.left.right.right_depth == 0

    assert b.root.right.value == 100
    assert b.root.right.left_depth == 0
    assert b.root.right.right_depth == 1

    assert b.root.right.right.value == 200
    assert b.root.right.right.left_depth == 0
    assert b.root.right.right.right_depth == 0


def test_building_to_fanciest02():
    """Everything works up to inserting 150."""
    from bst import BST
    b = BST()
    b.insert(100)
    b.insert(70)
    b.insert(80)
    b.insert(53)
    b.insert(60)
    b.insert(200)
    b.insert(150)
    assert b.root.value == 80
    assert b.root.left_depth == 2
    assert b.root.right_depth == 2

    assert b.root.left.value == 60
    assert b.root.left.left_depth == 1
    assert b.root.left.right_depth == 1

    assert b.root.left.left.value == 53
    assert b.root.left.left.left_depth == 0
    assert b.root.left.left.right_depth == 0

    assert b.root.left.right.value == 70
    assert b.root.left.right.left_depth == 0
    assert b.root.left.right.right_depth == 0

    assert b.root.right.value == 150
    assert b.root.right.left_depth == 1
    assert b.root.right.right_depth == 1

    assert b.root.right.left.value == 100
    assert b.root.right.left.left_depth == 0
    assert b.root.right.left.right_depth == 0

    assert b.root.right.right.value == 200
    assert b.root.right.right.left_depth == 0
    assert b.root.right.right.right_depth == 0


def test_building_to_fanciest03():
    """Everything works up to inserting 300."""
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
    assert b.root.value == 80
    assert b.root.left_depth == 2
    assert b.root.right_depth == 3

    assert b.root.left.value == 60
    assert b.root.left.left_depth == 1
    assert b.root.left.right_depth == 1

    assert b.root.left.left.value == 53
    assert b.root.left.left.left_depth == 0
    assert b.root.left.left.right_depth == 0

    assert b.root.left.right.value == 70
    assert b.root.left.right.left_depth == 0
    assert b.root.left.right.right_depth == 0

    assert b.root.right.value == 150
    assert b.root.right.left_depth == 1
    assert b.root.right.right_depth == 2

    assert b.root.right.left.value == 100
    assert b.root.right.left.left_depth == 0
    assert b.root.right.left.right_depth == 0

    assert b.root.right.right.value == 200
    assert b.root.right.right.left_depth == 0
    assert b.root.right.right.right_depth == 1

    assert b.root.right.right.right.value == 300
    assert b.root.right.right.right.left_depth == 0
    assert b.root.right.right.right.right_depth == 0

def test_delete_auto_adjust01(basic_setup):
    basic_setup.insert(5)
    basic_setup.delete(9)
    assert basic_setup.root.value == 10
    assert basic_setup.root.left_depth == 1
    assert basic_setup.root.right_depth == 0

    assert basic_setup.root.left.value == 5
    assert basic_setup.root.left.left_depth == 0
    assert basic_setup.root.left.right_depth == 0

def test_delete_auto_adjust02(fancier_setup):
    fancier_setup.delete(190)
    assert fancier_setup.root.value == 175
    assert fancier_setup.root.left_depth == 1
    assert fancier_setup.root.right_depth == 2

    assert fancier_setup.root.right.value == 200
    assert fancier_setup.root.right.left_depth == 1
    assert fancier_setup.root.right.right_depth == 0

    assert fancier_setup.root.right.left.value == 180
    assert fancier_setup.root.right.left.left_depth == 0
    assert fancier_setup.root.right.left.right_depth == 0

def test_delete_auto_adjust03(fancier_setup):
    fancier_setup.delete(175)
    assert fancier_setup.root.value == 180
    assert fancier_setup.root.left_depth == 1
    assert fancier_setup.root.right_depth == 2

    assert fancier_setup.root.left.value == 100
    assert fancier_setup.root.left.left_depth == 0
    assert fancier_setup.root.left.right_depth == 0

    assert fancier_setup.root.right.value == 190
    assert fancier_setup.root.right.left_depth == 0
    assert fancier_setup.root.right.right_depth == 1

    assert fancier_setup.root.right.right.value == 200
    assert fancier_setup.root.right.right.left_depth == 0
    assert fancier_setup.root.right.right.right_depth == 0

def test_delete_auto_adjust04(fanciest_setup):
    fanciest_setup.delete(80)
    assert fanciest_setup.root.value == 100
    assert fanciest_setup.root.left_depth == 2
    assert fanciest_setup.root.right_depth == 3

    assert fanciest_setup.root.right.value == 150
    assert fanciest_setup.root.right.right_depth == 2
    assert fanciest_setup.root.right.left_depth == 0

    assert fanciest_setup.root.right.right.value == 200
    assert fanciest_setup.root.right.right_depth == 1
    assert fanciest_setup.root.right.left_depth == 0
    #This one is not working correctly. BST won't adjust deleted nodes parents correctly.