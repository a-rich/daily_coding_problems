class Node:

    def __init__(self, val, left, right):
        self.data = val
        self.left = left
        self.right = right

def tree_equal(a, b):
    if a is None and b is None:
        return True

    if a.data != b.data:
        return False

    return tree_equal(a.left, b.left) and tree_equal(a.right, b.right)

def reconstruct_tree(preorder, inorder):
    keep_looking = True
    index = 0
    while keep_looking:
        root = preorder[index]
        try:
            root_index = inorder.index(root)
            keep_looking = False
        except ValueError:
            index += 1
    left = inorder[:root_index]
    right = inorder[root_index+1:]

    if not left and right:
        return Node(root,
                None,
                reconstruct_tree(preorder[1:], right))
    if not right and left:
        return Node(root,
                reconstruct_tree(preorder[:1], left),
                None)
    if not left and not right:
        return Node(root,
                None,
                None)

    return Node(root,
            reconstruct_tree(preorder[1:], left),
            reconstruct_tree(preorder[1:], right))

if __name__ == '__main__':
    preorder = ['a','b','c','d','e','f','g']
    inorder = ['d','b','e','a','f','c','g']

    tree_1 = Node('a', Node('b', Node('d', None, None), Node('e', None, None)),
            Node('c', Node('f', None, None), Node('g', None, None)))
    tree_2 = reconstruct_tree(preorder, inorder)

    assert tree_equal(tree_1, tree_2)

