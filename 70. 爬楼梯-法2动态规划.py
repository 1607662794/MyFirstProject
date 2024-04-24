#第二种方法主要使用动态规划，保留一个数作为存储，避免重复计算，其余的计算式进行拆解当前数等于下一个数或者下下个数
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        # def dp(n, memo):
        #     if n == 1:
        #         return 1
        #     elif n == 2:
        #         return 2
        #     elif memo[n] != 0:
        #         return memo[n]
        #     else:
        #         memo[n] = dp(n - 1, memo) + dp(n - 2, memo)
        #         return memo[n]
        #
        # return dp(n, [0] * (n + 1))
        method = [0 for i in range(n+1)]
        for i in range(1,n+1):
            if i == 1:
                method[i] = 1
            elif i == 2:
                method[i] = 2
            else:
                method[i] = method[i-1]+method[i-2]
        return method[-1]

solution = Solution()
print(solution.climbStairs(3))
