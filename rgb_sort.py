from __future__ import print_function

def rgb_sort(arr):
    shifts = 0
    for i,char in enumerate(list(arr)):
        if char == 'B':
            arr = arr[:i-shifts] + arr[i-shifts+1:]
            arr.append('B')
            shifts += 1

    for i,char in enumerate(list(arr)):
        if char == 'R':
            arr = arr[:i] + arr[i+1:]
            arr.insert(0, 'R')

    return arr

if __name__ == '__main__':
    arr = ['G','B','R','R','B','R','G']
    assert rgb_sort(arr) == ['R','R','R','G','G','B','B']
