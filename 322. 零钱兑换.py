class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # 这道题和刚才不大一样，最小单位不一定是1，一样，首先初始化，然后再从不同的硬币里面挑，动态规划函数的作用是
        dp = [float('inf')] * (amount + 1)  # 表示无穷大
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):  # 这样做有一个好处是避免了负值
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1


solution = Solution()
print(solution.coinChange([2], 3))
