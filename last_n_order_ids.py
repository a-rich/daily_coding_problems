class NOrdersQueue:
    def __init__(self, N):
        self.N = N
        self.queue = []

    def record(self, order_id):
        if len(self.queue) + 1 > self.N:
            self.queue.pop(0)
        self.queue.append(order_id)

    def get_last(self, i):
        if i > self.N:
            return "Queue only stores {} order IDs.".format(self.N)
        return self.queue[-i]

if __name__ == '__main__':
    queue = NOrdersQueue(5)

    orders = [1,2,3,4,5,6,7,8,9,10]
    for o in orders:
        queue.record(o)

    print(queue.get_last(6))
    print(queue.get_last(5))
    print(queue.get_last(2))
