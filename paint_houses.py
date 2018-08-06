from __future__ import print_function
from random import sample
import numpy as np

def min_cost(costs):
    i = 1
    cum_costs = [[0]*len(costs) for _ in costs[0]]

    for k in range(len(cum_costs)):
        cum_costs[k][0] = costs[0][k]

    while i < len(costs):
        for k in range(len(cum_costs)):
            cum_costs[k][i] = costs[i][k] + min([cum_costs[j][i-1]
                                                for j in range(len(cum_costs))
                                                if j != k])
        i += 1

    return min([c[-1] for c in cum_costs])


if __name__ == '__main__':
    n = 4
    k = 3
    paint_costs = [sample(range(n*k), k) for _ in range(n)]

    print('Solution for (N x K) cost matrix ({} houses x {} colors):\n{}'.format(
            n, k, np.matrix(paint_costs)))

    print('\nSolution has a cost of {}'.format(min_cost(paint_costs)))


