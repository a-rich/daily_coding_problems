from __future__ import print_function

class Node:
    def __init__(self, val=None):
        self.data = val
        self.next = None


class Stack:
    def __init__(self):
        self.stack = None

    def push(self, val):
        if not self.stack:
            self.stack = Node(val)
            return

        node = Node(val)
        node.next = self.stack
        self.stack = node

    def pop(self):
        val = self.stack.data
        self.stack = self.stack.next
        return val

    def max(self):
        if not self.stack:
            return None

        max_ = float('-inf')
        current = self.stack
        while current.next:
            if current.data > max_:
                max_ = current.data
            current = current.next
        return max_


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())
    print(s.max())
    s.pop()
    s.pop()
    print(s.max())
