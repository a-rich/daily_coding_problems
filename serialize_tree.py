from __future__ import print_function

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(tree):
    if not tree:
        return ''

    string_rep = ''
    queue = [tree]

    while queue:
        node = queue.pop(0)
        if node:
            string_rep += str(node.val) + ','
            queue.append(node.left)
            queue.append(node.right)
        else:
            string_rep += 'None,'

    return string_rep[:-1]

def deserialize(tree):
    if not tree:
        return None

    nodes = tree.split(',')
    root = Node(nodes[0])
    queue = [root]
    i = 1

    while queue:
        node = queue.pop(0)
        if not node:
            continue

        if nodes[i] != 'None':
            node.left = Node(nodes[i])
            queue.append(node.left)
        else:
            node.left = None
            queue.append(None)
        i += 1

        if nodes[i] != 'None':
            node.right = Node(nodes[i])
            queue.append(node.right)
        else:
            node.right = None
            queue.append(None)
        i += 1

    return root

if __name__ == '__main__':
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'

    node = Node('root', None, Node('right', Node('right.left'), Node('right.right')))
    assert deserialize(serialize(node)).right.right.val == 'right.right'
