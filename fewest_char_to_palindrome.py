def chars_to_palindrome(s):
    skip = 0

    def is_palindrome(substring):
        return substring == substring[::-1]

    while len(s)-1-skip > 0 and skip < len(s):
        if s[skip] == s[-1]:
            if is_palindrome(s[skip:]):
                return len(s[:skip][::-1])
        if s[0] == s[-1-skip]:
            if is_palindrome(s[:-1-skip+1]):
                return len(s[len(s)-skip:][::-1])
        skip += 1

    return len(s) - 1

if __name__ == '__main__':
    assert chars_to_palindrome('race') == 3
    assert chars_to_palindrome('racec') == 2
    assert chars_to_palindrome('raceca') == 1
    assert chars_to_palindrome('acecar') == 1
