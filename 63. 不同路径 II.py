#思路：仍然使用动态规划，将模式不断拆分，最后聚集到1,1的位置，有两种做法，一是避免碰到障碍物，而是可以碰到障碍物，但是一碰到即为0
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        def dp(x, y, memo):
            if x == 1 and y == 1 and obstacleGrid[0][0] != 1:
                return 1
            elif obstacleGrid[x-1][y-1] == 1:#如果当前的位置上放着障碍物，那边说明这条路是死的
                return 0
            elif memo[x-1][y-1] != None:#如果这条路之前走过，那么直接返回
                return memo[x-1][y-1]
            # elif x == 1 and y != 1 and obstacleGrid[x-1][y-2] != 1 or obstacleGrid[x-2][y-1] == 1 and obstacleGrid[x-1][y-2] != 1:#只能往左边走的情况：上边有障碍物，或者到达第一行了，并且左边不能是障碍物
            elif x == 1 and y != 1:#只能往左边走的情况：上边有障碍物，或者到达第一行了，并且左边不能是障碍物
                memo[x-1][y-1] = dp(x, y - 1, memo)
                return memo[x - 1][y - 1]
            # elif x != 1 and y == 1 and obstacleGrid[x-2][y-1] != 1 or obstacleGrid[x-1][y-2] == 1 and obstacleGrid[x-2][y-1] != 1:#只能往上边走的情况：左边有障碍物，或者到达第一列了，并且上边不能是障碍物
            elif x != 1 and y == 1:#只能往上边走的情况：左边有障碍物，或者到达第一列了，并且上边不能是障碍物
                memo[x-1][y-1] = dp(x - 1, y, memo)
                return memo[x - 1][y - 1]
            # elif obstacleGrid[x-2][y-1] == 1 and obstacleGrid[x-1][y-2] == 1:
            #     memo[x - 1][y - 1] = 0
            #     return memo[x - 1][y - 1]
            else:
                memo[x-1][y-1] = dp(x, y - 1, memo) + dp(x - 1, y, memo)
                return memo[x-1][y-1]
        return dp(len(obstacleGrid), len(obstacleGrid[0]), memo=[[None for i in range(len(obstacleGrid[0]))] for j in range(len(obstacleGrid))])

solution = Solution()
print(solution.uniquePathsWithObstacles([[1,0]]))