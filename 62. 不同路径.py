# 使用动态规划方法进行求解，记得需要一个东西进行存储，以空间换时间，存储已经计算出来的值，并在后期进行调用
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        def dp(x, y, memo):
            if x == 1 and y == 2 or x == 2 and y == 1 or x == 1 and y == 1:
                return 1
            elif memo[x-1][y-1] != 0:
                return memo[x-1][y-1]
            elif x == 1 and y != 1:
                memo[x-1][y-1] = dp(x, y - 1, memo)
                return memo[x - 1][y - 1]
            elif x != 1 and y == 1:
                memo[x-1][y-1] = dp(x - 1, y, memo)
                return memo[x - 1][y - 1]
            else:
                memo[x-1][y-1] = dp(x, y - 1, memo) + dp(x - 1, y, memo)
                return memo[x-1][y-1]
        return dp(m, n, memo=[[0 for i in range(n)] for j in range(m)])


solution = Solution()
print(solution.uniquePaths(1, 1))
