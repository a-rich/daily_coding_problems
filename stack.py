from __future__ import print_function

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.insert(0, val)

    def pop(self):
        return self.stack.pop(0)

    def max(self):
        try:
            return max(self.stack)
        except ValueError:
            return None

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
