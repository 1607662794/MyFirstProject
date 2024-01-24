#我的思路是，先寻找需要变为0的索引，然后再找一遍，将需要变为0的地方全部变为0
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0:
            return matrix
        row = []
        column = []
        #第一遍负责寻找需要变为0的指标索引，如果直接一遍顺序过去的话，之前经过的位置数值会被遗漏
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i not in row:
                        row.append(i)
                    if j not in column:
                        column.append(j)
        # 将需要变0的矩阵值全部变为0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in row or j in column:
                    matrix[i][j] = 0
        return matrix
solution = Solution()
print(solution.setZeroes([[1,1,1],[1,0,1],[1,1,1]]))
