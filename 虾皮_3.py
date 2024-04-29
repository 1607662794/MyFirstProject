class Solution:
    def maxCount(self, coins, costs):
        # write code here
        dp = [[0 for i in range(coins + 1)] for j in range(len(costs)+1)]
        costs.insert(0, 0)
        for i in range(1, len(costs)):
            for j in range(1, coins + 1):
                if j < costs[i]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i-1][j - costs[i]] + 1)
        return dp[len(costs)-1][coins]


solution = Solution()
print(solution.maxCount(10, [2, 1, 3, 4, 5]))
