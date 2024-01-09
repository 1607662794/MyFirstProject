# 我的思路是按照剥洋葱的方法，层层向内剥。
# 但我不知道为什么我的本地端结果和力扣结果不一致。
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
        else:
            global result
            result = list()
            return self.backtrace(0, matrix)

    def backtrace(self, number, matrix):
        global result
        if number == round(min(len(matrix), len(matrix[0])) / 2):
            return result
        # 如果短边除以2为奇数，则剩下一个单元或者一行或者一列单元，其余均是一个完整的圈
        # 接下来，i代表行的索引，j代表列的索引。
        elif min(len(matrix), len(matrix[0])) % 2 != 0 and len(matrix) == len(matrix[0]) and number + 1 == round(
                min(len(matrix), len(matrix[0])) / 2):
            result.append(matrix[number][number])
            return self.backtrace(number + 1, matrix)
        # 如果 m>n，则列多剩下了一次
        elif min(len(matrix), len(matrix[0])) % 2 != 0 and len(matrix) > len(matrix[0]) and number + 1 == round(
                min(len(matrix), len(matrix[0])) / 2):
            for i in range(len(matrix) - 2 * number):
                result.append(matrix[number + i][number])
            return self.backtrace(number + 1, matrix)
        # 如果 m<n，则行多剩下了一次
        elif min(len(matrix), len(matrix[0])) % 2 != 0 and len(matrix) < len(matrix[0]) and number + 1 == round(
                min(len(matrix), len(matrix[0])) / 2):
            for j in range(len(matrix[0]) - 2 * number):
                result.append(matrix[number][number + j])
            return self.backtrace(number + 1, matrix)
        else:
            for i in range(len(matrix[0]) - 2 * number - 1):
                result.append(matrix[number][number + i])
            for j in range(len(matrix) - 2 * number - 1):
                result.append(matrix[number + j][number + i + 1])
            for i in range(len(matrix[0]) - 2 * number - 1):
                result.append(matrix[number + j + 1][len(matrix[0]) - number - 1 - i])
            for j in range(len(matrix) - 2 * number - 1):
                result.append(matrix[len(matrix) - number - 1 - j][number])
            return self.backtrace(number + 1, matrix)


solution = Solution()
print(solution.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
