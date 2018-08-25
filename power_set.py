from __future__ import print_function
import sys

def power_set(input_set):
    sets = []

    for e in input_set:
        for s in list(sets):
            new_set = list(s)
            new_set.append(e)
            sets.append(new_set)
        sets.append([e])

    return sets

if __name__ == '__main__':
    input_set = list([1,2,3])
    sol = [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]
    assert all(s in sol for s in power_set(input_set))
