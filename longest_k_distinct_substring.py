from __future__ import print_function

def longest_k_distinct_substring(string, k):
    i, j = 0, 1
    sub_strings = []
    chars = set(list(string[i:j]))

    while j < len(string):

        while len(chars) <= k:
            chars.update(string[j])
            j += 1
        sub_strings.append(string[i:j-1])

        chars.discard(string[i])
        i += 1

    return max(sub_strings, key=lambda x: len(x))

if __name__ == '__main__':
    string = 'abcba'
    k = 2

    print(longest_k_distinct_substring(string, k))
