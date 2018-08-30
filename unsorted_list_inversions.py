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
    if len(arr) == 1:
        return arr, 0

    left, li = opt_count_inversions(arr[:len(arr)/2])
    right, ri = opt_count_inversions(arr[len(arr)/2:])
    merged = []

    i = j = 0
    inversions = li + ri
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            inversions += len(left) - i

    merged += left[i:]
    merged += right[j:]

    return merged, inversions

if __name__ == '__main__':
    arr = [2,4,1,3,5]
    assert opt_count_inversions(arr)[1] == 3

    arr = [5,4,3,2,1]
    assert opt_count_inversions(arr)[1] == 10
