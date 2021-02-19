import binarytree


# class Node:
#
#     def __init__(self, val, parent_node=None):
#         self.left = None
#         self.right = None
#         self.data = val
#         self.parent = None
#         if parent_node is not None:
#             self.parent = self
#         else:
#             self.parent = parent_node
#
#     def insert(self, data):
#         # Compare the new value with the parent node
#         if self.data:
#             if data < self.data:
#                 if self.left is None:
#                     self.left = Node(data)
#                 else:
#                     self.left.insert(data)
#             elif data > self.data:
#                 if self.right is None:
#                     self.right = Node(data)
#                 else:
#                     self.right.insert(data)
#         else:
#             self.data = data


def bst_query(x, root):
    if x.left is not None:
        x = x.left
        while x.right is not None:
            x = x.right
        return x
    y = binarytree.get_parent(root, x)
    while y is not None and x == y.left:
        x = y
        y = binarytree.get_parent(root, y)
    return y


# test_5 = Node(5)
# test_1 = Node(1, parent_node=test_5)
# test_3 = Node(3, parent_node=test_1)
# test_2 = Node(2, parent_node=test_3)
# test_4 = Node(4, parent_node=test_3)
# test_8 = Node(8, parent_node=test_5)
# test_6 = Node(6, parent_node=test_8)
# test_10 = Node(10, parent_node=test_8)
# test_7 = Node(7, parent_node=test_6)
# test_9 = Node(9, parent_node=test_10)

# test_5 = root = binarytree.Node(5)
# test_1 = root.left = binarytree.Node(1)
# test_3 = root.left.right = binarytree.Node(3)
# test_2 = root.left.right.left = binarytree.Node(2)
# test_4 = root.left.right.right = binarytree.Node(4)
#
# test_8 = root.right = binarytree.Node(8)
# test_6 = root.right.left = binarytree.Node(6)
# test_7 = root.right.left.right = binarytree.Node(7)
# test_10 = root.right.right = binarytree.Node(10)
# test_9 = root.right.right.left = binarytree.Node(9)

root = binarytree.Node(27)
root.left = binarytree.Node(14)
root.left.left = binarytree.Node(10)
root.left.right = binarytree.Node(19)
root.right = binarytree.Node(35)
root.right.left = binarytree.Node(31)
root.right.right = binarytree.Node(42)

# nodes_to_test = [bst_query(test_1, root),
#                  bst_query(test_2, root),
#                  bst_query(test_3, root),
#                  bst_query(test_4, root),
#                  bst_query(test_5, root),
#                  bst_query(test_6, root),
#                  bst_query(test_7, root),
#                  bst_query(test_8, root),
#                  bst_query(test_9, root),
#                  bst_query(test_10, root)]
#
# print(root)
# for node_to_test in nodes_to_test:
#     print(f"{node_to_test} is {node_to_test.val}" if node_to_test is not None else None)

print(bst_query(root, root).val)
print(bst_query(root.left, root).val)
print(bst_query(root.left.left, root))
print(bst_query(root.left.right, root).val)
# print(bst_query(root.left.right.left, root).val)
# print(bst_query(root.left.right.right, root).val)
print(bst_query(root.right, root).val)
print(bst_query(root.right.left, root).val)
print(bst_query(root.right.right, root).val)
# print(bst_query(root.right.right.left, root).val)
# print(bst_query(root.right.left.right, root).val)
