from BST import *

def second_largest_node(root):
    current_node = root
    while current_node.right:
        second_largest = current_node
        current_node = current_node.right
    if current_node.left:
        current_node = current_node.left
        second_largest = current_node
        while current_node.right:
            current_node = current_node.right
            second_largest = current_node
    return second_largest



if __name__ == '__main__':
    # Test case where max node has no children (2nd largest is max node's parent)
    r = Node(3)
    insert(r, Node(7))
    insert(r, Node(1))
    insert(r, Node(5))
    insert(r, Node(8))
    assert second_largest_node(r).data == 7

    # Test case where max node has left children (2nd largest is in-order
    # predecessor of max node)
    r = Node(8)
    insert(r, Node(3))
    insert(r, Node(10))
    insert(r, Node(1))
    insert(r, Node(6))
    insert(r, Node(14))
    insert(r, Node(4))
    insert(r, Node(7))
    insert(r, Node(13))
    assert second_largest_node(r).data == 13
