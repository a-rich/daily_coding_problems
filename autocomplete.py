from __future__ import print_function

def autocomplete(prefix, query_strings):
    results = []
    for q in query_strings:
        if q[:len(prefix)] == prefix:
            results.append(q)

    return results

if __name__ == '__main__':
    prefix = 'de'
    query_strings = ['dog', 'deer', 'deal']

    assert autocomplete(prefix, query_strings) == ['deer', 'deal']
