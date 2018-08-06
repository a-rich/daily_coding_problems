def find_missing(arr):
    arr.sort()
    i = 0

    while i < len(arr):
        if arr[i] < 1:
            i += 1
            continue
        if arr[i-1] > 0 and arr[i] != arr[i-1] + 1:
            return arr[i-1] + 1
        i += 1

    return arr[-1] + 1

if __name__ == '__main__':
    test_1 = [3,4,-1,1]
    test_2 = [1,2,0]

    assert find_missing(test_1) == 2
    assert find_missing(test_2) == 3


