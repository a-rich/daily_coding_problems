def two_sum(nums, k):
    d = {}

    for n in nums:
        if n in d:
            return True
        else:
            d[k-n] = 1

    return False

if __name__ == '__main__':

    assert two_sum([10,15,2,7], 17) == True
    assert two_sum([1,2,3], 4) == True
    assert two_sum([1,2,3], 5) == True
    assert two_sum([1,2,3], 6) == False
