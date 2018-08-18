def dp_num_decodings(digits):
    n = len(digits) + 1
    dp = [0] * n
    dp[0] = dp[1] = 1

    for i in range(2, n):
        dp[i] = 0

        if digits[i-1] > '0':
            dp[i] = dp[i-1]

        if digits[i-2] == '1' or (digits[i-2] == '2' and digits[i-1] < '7'):
            dp[i] += dp[i-2]

    return dp[n-1]

def crazy_num_decodings(s):
    """Stole this from online -- pissed that I'd never think of this"""

    v, w, p = 0, int(s>''), ''
    for d in s:
        v, w, p = w, (d>'0')*w + (9<int(p+d)<27)*v, d
    return w

if __name__ == '__main__':
    assert dp_num_decodings('111') == 3
    assert crazy_num_decodings('111') == 3
