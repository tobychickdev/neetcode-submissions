class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        # dp[m][n] is the number of possible unique paths that can be taken from dp[0][0] to dp[m][n]
        # dp[m][n] = (dp[m][n-1] + 1) + (dp[m-1][n] + 1)
        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    continue
                if i > 0: # has above
                    if j > 0: # has left
                        dp[i][j] = dp[i][j-1] + dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[m-1][n-1]
                    



        