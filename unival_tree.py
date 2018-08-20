from BinaryTree import BinaryTree, Node

def num_unival_trees(node):
    count = [0]
    helper(node, count)

    return count[0]

def helper(node, count):
    if node is None:
        return True

    left = helper(node.left, count)
    right = helper(node.right, count)

    if left == False or right == False:
        return False

    if node.left and node.data != node.left.data:
        return False

    if node.right and node.data != node.right.data:
        return False

    count[0] += 1

    return True



if __name__ == '__main__':
    bt = BinaryTree(0)
    bt.root.left = Node(1)
    bt.root.right = Node(0)
    bt.root.right.left = Node(1)
    bt.root.right.right = Node(0)
    bt.root.right.left.left = Node(1)
    bt.root.right.left.right = Node(1)

    assert num_unival_trees(bt.root) == 5


