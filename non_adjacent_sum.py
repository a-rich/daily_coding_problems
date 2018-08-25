def recursive_non_adjacent_max_sum(arr, i):
    if i == 0:
        return arr[0]
    if i == 1:
        return max(arr[0], arr[1])
    return max(non_adjacent_sum(arr, i-1), arr[i] + non_adjacent_sum(arr, i-2))

def opt_non_adjacent_max_sum(arr):
    prev = next_prev = max_ = 0
    for i in range(len(arr)):
        if i == 0:
            max_ = arr[i]
        elif i == 1:
            max_ = max(arr[0], arr[i])
        else:
            max_ = max(prev, arr[i] + next_prev)

        next_prev = prev
        prev = max_

    return max_

if __name__ == '__main__':
    arr = [2,4,6,2,5]
    assert opt_non_adjacent_max_sum(arr) == 13

    arr = [5,1,1,5]
    assert opt_non_adjacent_max_sum(arr) == 10
