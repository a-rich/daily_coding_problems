from __future__ import print_function

def subarray_max_values(arr, k):
    if not arr or len(arr) < k:
        return None

    queue = []
    for i in range(len(arr)):
        while queue:
            if arr[i] >= arr[queue[-1]]:
                queue.pop()
            else:
                break
        queue.append(i)
        begin = i - k + 1

        if begin >= 0:
            print(arr[queue[0]])
            if begin == queue[0]:
                queue.pop(0)

if __name__ == '__main__':
    subarray_max_values([10,5,2,7,8,7], 3)
