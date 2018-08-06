from __future__ import print_function

def find_missing(arr):
    arr.sort()
    i = 0

    while i < len(arr):
        if arr[i] < 1:
            continue
        if arr[i] != arr[i-1] + 1:
            return arr[i-1] + 1

    return arr[-1] + 1

if __name__ == '___main__':
    test_1 = [3,4,-1,1]
    test_2 = [1,2,0]

    assert find_missing(test_1) == 2
    assert find_missing(test_2) == 3
