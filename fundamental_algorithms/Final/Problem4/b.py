# The mid-range M of set S is defined as the mean of its smallest and largest
# values: M = (min(S) + max(S))=2. For example, the mid-range of f2, 3, 5,7g is 4.5.
# Give an efficient procedure BST-MID that returns the mid-range of keys of a given binary search tree.
# State its running time. Do not assume the existence of any helper functions.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def binary_tree_min(bst_root):
    if bst_root is None:
        return float('inf')
    minimum = bst_root.data
    min_of_left = binary_tree_min(bst_root.left)
    min_of_right = binary_tree_min(bst_root.right)
    if min_of_left < minimum:
        minimum = min_of_left
    if min_of_right < minimum:
        minimum = min_of_right
    return minimum


def binary_tree_max(bst_root):
    if bst_root is None:
        return float('-inf')
    maximum = bst_root.data
    max_of_left = binary_tree_max(bst_root.left)
    max_of_right = binary_tree_max(bst_root.right)
    if max_of_left > maximum:
        maximum = max_of_left
    if max_of_right > maximum:
        maximum = max_of_right
    return maximum


def bst_mid(tree_root):
    return (binary_tree_min(tree_root) + binary_tree_max(tree_root)) / 2


root = Node(2)
root.left = Node(3)
root.right = Node(5)
root.left.right = Node(7)

print(bst_mid(root))
