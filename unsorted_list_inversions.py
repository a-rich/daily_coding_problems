from __future__ import print_function
import heapq

def naive_count_inversions(arr):
    i = count = 0

    while i < len(arr):
        j = i + 1
        while j < len(arr):
            if i < j and arr[i] > arr[j]:
                count += 1
            j += 1
        i += 1

    return count

def opt_count_inversions(arr):
    inversions = 0
    heap = list(arr)
    heapq.heapify(heap)

    while heap:
        for n in arr:
            if n > heap[0]:
                inversions += 1
            elif n == heap[0]:
                heapq.heappop(heap)
                break

    return inversions

if __name__ == '__main__':
    arr = [2,4,1,3,5]
    assert opt_count_inversions(arr) == 3

    arr = [5,4,3,2,1]
    assert opt_count_inversions(arr) == 10
