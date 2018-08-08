def reconstruct_words(d, string):
    i,j = 0,1
    words = []

    while string:
        sub = string[i:j]
        if sub in d:
            words.append(sub)
            string = string[j:]
            i,j = 0,1
        else:
            j += 1

    return words

if __name__ == '__main__':
    d = {'quick': 1,
         'brown': 1,
         'the': 1,
         'fox': 1
         }
    string = 'thequickbrownfox'
    assert reconstruct_words(d, string) == ['the', 'quick', 'brown', 'fox']

    d = {'bed': 1,
         'bath': 1,
         'bedbath': 1,
         'and': 1,
         'beyond': 1
         }
    string = 'bedbathandbeyond'
    assert reconstruct_words(d, string) == ['bed', 'bath', 'and', 'beyond'] \
            or reconstruct_words(d, string) == ['bedbath', 'and', 'beyond']
