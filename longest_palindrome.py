def longest_palindrome(string):
    skip = 0

    def is_palindrome(substring):
        return substring == substring[::-1]

    while skip < len(string)-1:
        if string[skip] == string[-1]:
            if is_palindrome(string[skip:]):
                return string[skip:]
        if string[0] == string[-1-skip]:
            if is_palindrome(string[:-skip]):
                return string[:-skip]
        skip += 1

    return 'No palindrome present.'

if __name__ == '__main__':
    assert longest_palindrome('racecar') == 'racecar'
    assert longest_palindrome('raceca') == 'aceca'
    assert longest_palindrome('acecar') == 'aceca'
    assert longest_palindrome('race') == 'No palindrome present.'
