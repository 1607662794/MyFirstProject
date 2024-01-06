# 我的思路是：每一边的len(n)-1，依次进行旋转，一共旋转4遍（对应四个边），旋转的索引只需要针对x，y进行追踪就可以，然后一圈一圈的进行迭代。
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix) // 2):
            for j in range(len(matrix) - 1 - 2 * i):
                value_1 = matrix[i][i + j]
                matrix[i][i + j] = matrix[len(matrix) - i - j - 1][i]  # 上侧边等于左侧边
                matrix[len(matrix) - i - j - 1][i] = matrix[len(matrix) - 1 - i][len(matrix) - 1 - i - j]  # 左侧边等于下侧边
                matrix[len(matrix) - 1 - i][len(matrix) - 1 - i - j] = matrix[i + j][len(matrix) - 1 - i]  # 下侧边等于右侧边
                matrix[i + j][len(matrix) - 1 - i] = value_1  # 右侧边等于上侧边
        return matrix


solution = Solution()
print(solution.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
