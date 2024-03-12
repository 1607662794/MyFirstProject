# 对于这道题，我的思路是不断对比对角线上的值，如果等于的话，就相当于直接找到了，如果小于当前值的话，则需要查询上一个对角线元素对应的横轴及纵轴，如果大于当前值的话，则查看下一个对角线元素，如果到了边缘位置，则查询当前对角线元素的横轴和纵轴即可。
# Leecode是从右上角开始遍历，如果 target 的值小于当前值，也就意味着当前值所在的列肯定不会存在 target 了，可以把当前列去掉，从新的右上角的值开始遍历。
# 同理，如果 target 的值大于当前值，也就意味着当前值所在的行肯定不会存在 target 了，可以把当前行去掉，从新的右上角的值开始遍历。比我的思路要简单很多。我操了
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        def find(i, j):
            for x in range(i):
                if matrix[x][j] == target:
                    return True
            for y in range(j):
                if matrix[i][y] == target:
                    return True
            return False

        i, j = 0, 0

        while True:
            if i > len(matrix)-1 or j > len(matrix[0])-1 or (matrix[i][j] < target and i == len(matrix) - 1 and j == len(matrix[0]) - 1) or (matrix[i][j] > target and i == 0):  # 找不到的两种情况
                return False
            elif matrix[i][j] == target:
                return True
            elif i == len(matrix) - 1 and j != len(matrix[0]) - 1:  # 剩下的空间其实也是有可能找到的
                if find(i,j):
                    return True
                matrix = [matrix[i][j + 1:] for i in range(len(matrix))]
                return self.searchMatrix(matrix, target)
            elif j == len(matrix[0]) - 1 and i != len(matrix) - 1:  # 剩下的空间其实也是有可能找到的
                if find(i,j):
                    return True
                matrix = [matrix[i][:] for i in range(i + 1, len(matrix))]
                return self.searchMatrix(matrix, target)
            elif matrix[i][j] > target:
                if find(i, j):
                    return True
                else:
                    i += 1
                    j += 1
            else:
                i += 1
                j += 1


solution = Solution()
print(solution.searchMatrix(
    [[3,5,9,9,9,11],[5,8,13,13,16,17],[10,10,14,14,16,19],[15,18,20,24,26,26],[20,24,29,32,37,41]], target=32))
