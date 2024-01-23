# 我的思路还是动态规划，对于抵达当前位置的最小路径，等于抵达它的上和左边最小路径的最小值，留出一个memo作为记录，避免重复计算，不断进行拆解
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def dp(x, y, memo):
            if x == 1 and y == 1:
                return grid[0][0]
            elif memo[x - 1][y - 1] != 0:
                return memo[x - 1][y - 1]
            elif x == 1 and y != 1:
                memo[x - 1][y - 1] = dp(x, y - 1, memo) + grid[x - 1][y - 1]
                return memo[x - 1][y - 1]
            elif x != 1 and y == 1:
                memo[x - 1][y - 1] = dp(x - 1, y, memo) + grid[x - 1][y - 1]
                return memo[x - 1][y - 1]
            else:
                memo[x - 1][y - 1] = min(dp(x, y - 1, memo), dp(x - 1, y, memo)) + grid[x - 1][y - 1]
                return memo[x - 1][y - 1]

        return dp(len(grid), len(grid[0]), memo=[[0 for i in range(len(grid[0]))] for j in range(len(grid))])

solution = Solution()
print(solution.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
