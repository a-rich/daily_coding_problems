def subset_sum(arr, k):
    if not arr or k <= 0:
        return None

    if arr[0] == k:
        return [arr[0]]

    include = subset_sum(arr[1:], k-arr[0])
    if include:
        return [arr[0]] + include

    return subset_sum(arr[1:], k)


if __name__ == '__main__':
    arr = [12, 1, 61, 5, 9, 2]
    k = 24
    assert subset_sum(arr, k) == [12, 1, 9, 2]
