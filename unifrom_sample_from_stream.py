import random

class StreamSample:
    def __init__(self):
        self.count = 0

    def sample(self, item):
        self.count += 1
        if self.count == 1:
            print(item)
        gen = random.randint(0, self.count-1)
        if gen == self.count-2:
            print(item)

if __name__ == '__main__':
    ss = StreamSample()
    items = list(range(0, 100))
    for i in items:
        ss.sample(i)
