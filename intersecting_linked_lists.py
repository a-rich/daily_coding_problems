class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

    def get_value(self):
        return self.value

    def set_next(self, node):
        self.next = node

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return "Node({})".format(self.value)

class LinkedList:
    def __init__(self, nodes=[]):
        self.head = None

        if nodes:
            self.head = Node(nodes.pop(0))
            last = self.head
            while nodes:
                temp = Node(nodes.pop(0))
                last.set_next(temp)
                last = temp

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def __str__(self):
        return "[{}]".format(", ".join(map(str, self)))

    def __repr__(self):
        return "LinkedList({})".format(self)

def find_intersection(ll_a, ll_b):
    cache = {}

    for node in ll_a:
        cache[node.get_value()] = node

    for node in ll_b:
        if node.get_value() in cache:
            temp = node

            if temp.next is None and cache[temp.get_value()].next is None:
                return node

            def helper(temp):
                while temp.next:
                    if temp.next.get_value() == cache[temp.get_value()].next.get_value():
                        temp = temp.next
                    else:
                        return None

                return node

            result = helper(temp)
            if result:
                return result

    return "These linked lists do not intersect."

if __name__ == '__main__':
    # Tests two LinkedLists that intersect at their final nodes.
    ll_a = LinkedList([1,2,3])
    ll_b = LinkedList([5,4,3])
    print(find_intersection(ll_a, ll_b))

    # Tests two LinkedLists that do not intersect at all.
    ll_a = LinkedList([1,2,3])
    ll_b = LinkedList([6,5,4])
    print(find_intersection(ll_a, ll_b))

    # Tests two linked lists that intersect somewhere in the middle.
    ll_a = LinkedList([3,7,8,10])
    ll_b = LinkedList([99,1,8,10])
    print(find_intersection(ll_a, ll_b))

    # Tests two linked lists that have matching values at some point prior to
    # their intersecting nodes.
    ll_a = LinkedList([3,7,2,8,10])
    ll_b = LinkedList([99,1,7,8,10])
    print(find_intersection(ll_a, ll_b))



