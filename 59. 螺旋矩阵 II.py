# 我的思路是把之前的螺旋矩阵代码改写一下，使之适应新的情况，还是出现了之前的问题，跑出来的结果和力扣上的不一样
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        if n == 0:
            return []
        elif n==1:
            return [1]
        else:
            global matrix
            matrix = [[1 for _ in range(n)] for _ in range(n)]
            return self.add_element(n, 0, 1)

    def add_element(self, n, number, add_number):  # n代表总的阶数，number代表当前运行到第几层了
        global matrix

        if number+1 == round(n / 2) and n % 2 != 0:  # 如果最后剩下一个单元格，那么填充该单元格，并返回整个矩阵
            matrix[number][number] = add_number
            return matrix
        elif number == round(n / 2) and n % 2 == 0: ##对于不剩单元格的情况，执行完全部后，返回矩阵
            return matrix
        else:
            # 接下来，i代表行的索引，j代表列的索引。
            for i in range(n - 2 * number - 1):
                matrix[number][number + i] = add_number
                add_number += 1
            for j in range(n - 2 * number - 1):
                matrix[number + j][number + i + 1] = add_number
                add_number += 1
            for i in range(n - 2 * number - 1):
                matrix[number + j + 1][len(matrix[0]) - number - 1 - i] = add_number
                add_number += 1
            for j in range(n - 2 * number - 1):
                matrix[len(matrix) - number - 1 - j][number] = add_number
                add_number += 1
            return self.add_element(n, number + 1, add_number)


solution = Solution()
print(solution.generateMatrix(2))
