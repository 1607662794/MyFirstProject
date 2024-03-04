# 我的思路是直接将原来的表格给改了，所有的表格存储的值是当前位置左子矩阵的求和
class Solution(object):
    def countSubmatrices(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        sum_grid = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        def sum_semigrid(row, column):  # 该函数用于更新表格内容，使其内容变为当前子阵的和
            if row == 0 and column == 0:
                sum_grid[row][column] = grid[row][column]
            elif row == 0:
                sum_grid[row][column] = sum_grid[row][column-1] + grid[row][column]
            elif column == 0:
                sum_grid[row][column] += sum_grid[row-1][column]
            else:
                sum_grid[row][column] += sum_grid[row][column-1] + grid[row - 1][column] + grid[row][column]

        result = 0
        for i in range(len(grid)):  # 表示有几行
            for j in range(len(grid[0])):  # 表示有几列
                sum_semigrid(i, j)
                if grid[i][j] <= k:
                    result += 1
                else:
                    break
        return result

soluiton = Solution()
print(soluiton.countSubmatrices([[7,2,9],[1,5,0],[2,6,6]], 20))
