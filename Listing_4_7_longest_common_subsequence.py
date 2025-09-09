def longest_common_subsequence(A, B):
    dp = [[0 for i in range(len(B))] for i in range(len(A))]

    # fill in the first row
    if A[0] == B[0]:
        dp[0][0] = 1
    else:
        dp[0][0] = 0

    for i in range(1, len(B)):
        if B[i] == A[0]:
            dp[0][i] = dp[0][i-1] + 1
        else:
            dp[0][i] = dp[0][i-1]

    # fill in the first col
    for i in range(1, len(A)):
        if A[i] == B[0]:
            dp[i][0] = dp[i-1][0] + 1
        else:
            dp[i][0] = dp[i-1][0]

    # fill in the rest of the matrix
    for i in range(1, len(A)):
        for j in range(1, len(B)):
            if A[i] == B[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]

if __name__ == '__main__':
    print (longest_common_subsequence('nature', 'nurture'))

