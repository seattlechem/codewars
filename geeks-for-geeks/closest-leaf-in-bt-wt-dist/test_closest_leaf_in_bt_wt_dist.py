"""Test cases."""
from closest_leaf_in_bt_wt_dist import Node, find_closest


root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.right.left = Node('E')
root.right.right = Node('F')
root.right.left.left = Node('G')
root.right.left.left.left = Node('I')
root.right.left.left.right = Node('J')
root.right.right.right = Node('H')
root.right.right.right.left = Node('K')


def test_h():
    """."""
    result = find_closest(root, 'H')
    assert result == {'val': ['K'], 'dist': [1]}


def test_c():
    """."""
    result = find_closest(root, 'C')
    assert result == {'val': ['B'], 'dist': [2]}


def test_b():
    """."""
    result = find_closest(root, 'B')
    assert result == {'val': ['B'], 'dist': [0]}


def test_e():
    """."""
    result = find_closest(root, 'E')
    assert result == {'val': ['I', 'J'], 'dist': [2, 2]}
