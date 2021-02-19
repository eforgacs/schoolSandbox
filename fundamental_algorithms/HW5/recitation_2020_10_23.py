
for value in preorder:
    node.left = inorder[value:]
    node.right = inorder[:value]
    tree.append(node)
