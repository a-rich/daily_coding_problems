from __future__ import print_function
from math import log
from timeit import timeit
from functools import reduce

def prod_div(arr):
    # Make a copy of the input array to make this a functional solution.
    arr = list(arr)

    # If there is only one 0 in the array, the solution should have the product
    # of all the other numbers at that index and 0 in all other indices.
    if arr.count(0) == 1:
        zero_index = arr.index(0)
        arr[zero_index] = reduce(lambda x,y: x*y, arr[:zero_index] + arr[zero_index+1:])
        arr = [0 if i != zero_index else x for i,x in enumerate(arr)]
        return arr

    # If there is more than one 0 in the array, the solution is all zeros.
    elif arr.count(0) > 1:
        return [0 for x in arr]

    # Otherwise, each index of the solution is the product divided by the
    # original value at that index.
    answer = []
    product = reduce(lambda x,y: x*y, arr)
    for i in range(len(arr)):
        answer.append(int(product / arr[i]))
    return answer

def prod_no_div_n_squared(arr):
    # Make a copy of the input array to make this a functional solution.
    arr = list(arr)

    # If there is only one 0 in the array, the solution should have the product
    # of all the other numbers at that index and 0 in all other indices.
    if arr.count(0) == 1:
        zero_index = arr.index(0)
        arr[zero_index] = reduce(lambda x,y: x*y, arr[:zero_index] + arr[zero_index+1:])
        arr = [0 if i != zero_index else x for i,x in enumerate(arr)]
        return arr

    # If there is more than one 0 in the array, the solution is all zeros.
    elif arr.count(0) > 1:
        return [0 for x in arr]

    answer = []
    for i in range(len(arr)):
        copy = arr[:i] + arr[i+1:]
        product = reduce(lambda x,y: x*y, copy)
        answer.append(product)

    return answer

def prod_no_div_log_trick(arr):
    # Make a copy of the input array to make this a functional solution.
    arr = list(arr)

    # If there is only one 0 in the array, the solution should have the product
    # of all the other numbers at that index and 0 in all other indices.
    if arr.count(0) == 1:
        zero_index = arr.index(0)
        arr[zero_index] = reduce(lambda x,y: x*y, arr[:zero_index] + arr[zero_index+1:])
        arr = [0 if i != zero_index else x for i,x in enumerate(arr)]
        return arr

    # If there is more than one 0 in the array, the solution is all zeros.
    elif arr.count(0) > 1:
        return [0 for x in arr]

    # Here we can leverage the log property: log(a/b) = log(a) - log(b)
    # to circumvent the division operation...just exponentiate the result of
    # subracting the log of the value at each index by the log of the product.
    answer = []
    product = reduce(lambda x,y: x*y, arr)
    for i in range(len(arr)):
        answer.append(int(round(10**(log(product, 10)-log(arr[i], 10)))))
    return answer

def prod_no_div_memo(arr):
    # Make a copy of the input array to make this a functional solution.
    arr = list(arr)

    # This solution remains correct even without this `if-else` block, but the
    # runtime is much slower.
    if arr.count(0) == 1:
        zero_index = arr.index(0)
        arr[zero_index] = reduce(lambda x,y: x*y, arr[:zero_index] + arr[zero_index+1:])
        arr = [0 if i != zero_index else x for i,x in enumerate(arr)]
        return arr

    elif arr.count(0) > 1:
        return [0 for x in arr]

    answer = []
    cum_prod = 1
    for i in range(len(arr)):
        answer.append(cum_prod)
        cum_prod *= arr[i]

    cum_prod = 1
    for i in reversed(range(len(arr))):
        answer[i] *= cum_prod
        cum_prod *= arr[i]

    return answer


if __name__ == '__main__':
    # Set up the 3 different cases involving 0, 1, or 2+ zeros.
    arr_1 = list(range(1, 17))
    arr_2 = [0] + list(range(1, 17))
    arr_3 = [0, 0] + list(range(1, 17))

    # Test equality of solutions.
    sol_1_1 = prod_div(arr_1)
    sol_1_2 = prod_no_div_n_squared(arr_1)
    sol_1_3 = prod_no_div_log_trick(arr_1)
    sol_1_4 = prod_no_div_memo(arr_1)

    sol_2_1 = prod_div(arr_2)
    sol_2_2 = prod_no_div_n_squared(arr_2)
    sol_2_3 = prod_no_div_log_trick(arr_2)
    sol_2_4 = prod_no_div_memo(arr_2)

    sol_3_1 = prod_div(arr_3)
    sol_3_2 = prod_no_div_n_squared(arr_3)
    sol_3_3 = prod_no_div_log_trick(arr_3)
    sol_3_4 = prod_no_div_memo(arr_3)

    sol_1_valid = all(sol_1_1[i] == sol_1_2[i] == sol_1_3[i] == sol_1_4[i] for i in range(len(arr_1)))
    sol_2_valid = all(sol_2_1[i] == sol_2_2[i] == sol_2_3[i] == sol_2_4[i] for i in range(len(arr_2)))
    sol_3_valid = all(sol_3_1[i] == sol_3_2[i] == sol_3_3[i] == sol_3_4[i] for i in range(len(arr_3)))

    print('All methods have the same solution when:')
    print('\tall values are non-zero:', sol_1_valid)
    print('\tone zero value is present:', sol_2_valid)
    print('\tmore than one zero value is present:', sol_3_valid)

    # Time the different solutions.
    sol_1_time = timeit('prod_div(arr_1)', 'from __main__ import prod_div, arr_1', number=100000)
    sol_2_time = timeit('prod_no_div_n_squared(arr_1)', 'from __main__ import prod_no_div_n_squared, arr_1', number=100000)
    sol_3_time = timeit('prod_no_div_log_trick(arr_1)', 'from __main__ import prod_no_div_log_trick, arr_1', number=100000)
    sol_4_time = timeit('prod_no_div_memo(arr_1)', 'from __main__ import prod_no_div_memo, arr_1', number=100000)

    print('\nAll four solutions have the same runtime for cases that' \
          '\ninclude zero values so their runtimes aren\'t compared here...')
    print('\nThe division solution has the following runtimes for the non-zero case:\n\t', sol_1_time)
    print('The O(n^2) solution has the following runtimes for the non-zero case:\n\t', sol_2_time)
    print('The log trick solution has the following runtimes for the non-zero case:\n\t', sol_3_time)
    print('The memo solution has the following runtimes for the non-zero case:\n\t', sol_4_time)
