import math


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''版本一，先遍历背包, 再遍历物品'''
        # 自底向上
        # 初始化
        nums = [i ** 2 for i in range(1, n + 1) if i ** 2 <= n]
        dp = [n] * (n + 1)
        dp[0] = 0
        # 遍历背包
        for j in range(1, n + 1):
            # 遍历物品
            for num in nums:
                if j >= num:
                    dp[j] = min(dp[j], dp[j - num] + 1)
        return dp[n]



solution = Solution()
print(solution.numSquares(12))