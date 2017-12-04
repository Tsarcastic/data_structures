"""."""

import pytest


@pytest.fixture
def basic_setup():
    """A basic setup with two numbers."""
    from bst_balancing import BST
    b = BST()
    b.insert(9)
    b.insert(10)
    return b


@pytest.fixture
def fancy_setup():
    """A more complicated setup."""
    from bst_balancing import BST
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
    from bst_balancing import BST
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
    from bst_balancing import BST
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


   

def test_building_to_fancier02():
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


#def test_restructure04(fancier_setup):
    """Test the restructure method on fancy_setup tree."""
    #assert fancier_setup.root.right.value == 100


#def test_restructure05(fancier_setup):
    """Test the restructure method on fancy_setup tree."""
    #fancier_setup.delete(200)
    #assert fancier_setup.root.left.value == 180
