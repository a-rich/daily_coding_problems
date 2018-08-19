from __future__ import print_function
import heapq

class RunningMedian:

    def __init__(self, nums=[]):
        self.max_heap, self.min_heap = [], []
        heapq.heapify(self.max_heap)
        heapq.heapify(self.min_heap)

        if nums:
            for _ in range(len(nums)):
                self.add_num(nums.pop(0))

    def add_num(self, num):
        if self.max_heap and num >= -self.max_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)

        if len(self.min_heap) - len(self.max_heap) > 1:
            move_num = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -move_num)
        elif len(self.max_heap) - len(self.min_heap) > 1:
            move_num = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, move_num)

    def get_median(self):
        if len(self.min_heap) > len(self.max_heap):
            return float(self.min_heap[0])
        elif len(self.max_heap) > len(self.min_heap):
            return float(-self.max_heap[0])
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2.


if __name__ == '__main__':
    nums = [2,1,5,7,2,0,5]
    rm = RunningMedian()

    for num in nums:
        rm.add_num(num)
        print('Adding {} -- median is {}'.format(num, rm.get_median()))
