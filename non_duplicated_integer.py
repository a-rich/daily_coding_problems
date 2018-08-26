def non_duplicated_integer(arr):
    return int(((3 * sum(set(arr))) - sum(arr)) / 2)

if __name__ == '__main__':
    arr = [6,1,3,3,3,6,6]
    assert non_duplicated_integer(arr) == 1

    arr = [13,19,13,13]
    assert non_duplicated_integer(arr) == 19
