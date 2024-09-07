# 我的思路是按照剥洋葱的方法，层层向内剥。
# 但我不知道为什么我的本地端结果和力扣结果不一致。
class Solution(object):
    def spiralOrder(self, matrix):
    #     """
    #     :type matrix: List[List[int]]
    #     :rtype: List[int]
    #     """
    #     if matrix == []:
    #         return []
    #     else:
    #         global result
    #         result = list()
    #         return self.backtrace(0, matrix)
    # 
    # def backtrace(self, number, matrix):
    #     global result
    #     if number == round(min(len(matrix), len(matrix[0])) / 2):
    #         return result
    #     # 如果短边除以2为奇数，则剩下一个单元或者一行或者一列单元，其余均是一个完整的圈
    #     # 接下来，i代表行的索引，j代表列的索引。
    #     elif min(len(matrix), len(matrix[0])) % 2 != 0 and len(matrix) == len(matrix[0]) and number + 1 == round(
    #             min(len(matrix), len(matrix[0])) / 2):
    #         result.append(matrix[number][number])
    #         return self.backtrace(number + 1, matrix)
    #     # 如果 m>n，则列多剩下了一次
    #     elif min(len(matrix), len(matrix[0])) % 2 != 0 and len(matrix) > len(matrix[0]) and number + 1 == round(
    #             min(len(matrix), len(matrix[0])) / 2):
    #         for i in range(len(matrix) - 2 * number):
    #             result.append(matrix[number + i][number])
    #         return self.backtrace(number + 1, matrix)
    #     # 如果 m<n，则行多剩下了一次
    #     elif min(len(matrix), len(matrix[0])) % 2 != 0 and len(matrix) < len(matrix[0]) and number + 1 == round(
    #             min(len(matrix), len(matrix[0])) / 2):
    #         for j in range(len(matrix[0]) - 2 * number):
    #             result.append(matrix[number][number + j])
    #         return self.backtrace(number + 1, matrix)
    #     else:
    #         for i in range(len(matrix[0]) - 2 * number - 1):
    #             result.append(matrix[number][number + i])
    #         for j in range(len(matrix) - 2 * number - 1):
    #             result.append(matrix[number + j][number + i + 1])
    #         for i in range(len(matrix[0]) - 2 * number - 1):
    #             result.append(matrix[number + j + 1][len(matrix[0]) - number - 1 - i])
    #         for j in range(len(matrix) - 2 * number - 1):
    #             result.append(matrix[len(matrix) - number - 1 - j][number])
    #         return self.backtrace(number + 1, matrix)
        result = []
        while matrix:
            deal_object = matrix.pop(0)  # 若矩阵不为空，那么肯定有一行存在。
            for i in range(len(deal_object)):  # 上边一行。
                result.append(deal_object.pop(0))

            for i in range(len(matrix)):  # 右边一列。
                result.append(matrix[i].pop())
            for i in range(len(matrix)):  # 右边一列。
                if not matrix[0]:
                    matrix.pop()

            if len(matrix) > 0:  # 存在将右边一列删除后，矩阵变空的情形，所以在这儿加一个判断条件。
                deal_object = matrix.pop()
                for i in range(len(deal_object)):  # 上边一行。
                    result.append(deal_object.pop())

            for i in range(len(matrix)):  # 左边一列。
                result.append(matrix[-i - 1].pop(0))
            for i in range(len(matrix)):  # 左边一列。
                if not matrix[0]:
                    matrix.pop()
        return result

solution = Solution()
print(solution.spiralOrder([[7],[9],[6]]))
