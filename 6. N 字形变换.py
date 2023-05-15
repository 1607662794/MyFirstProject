import math
'''整个过程就像是在进行密码学，编码解码'''
class Solution(object):
    def convert(self, s, numRows):
        a = ''
        '''输出新的字符'''
        if numRows== 1:
            return s

        matrix = self.encode(s, numRows)
        # j代表行
        for j in range(numRows):
            # i代表列
            for i in range(math.ceil(len(s) / (2 * numRows - 2)) * (numRows - 1)):
                if matrix[i][j]:
                    a = ''.join([a, matrix[i][j]])
        return a
    def encode(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        '''建立空矩阵'''
        matrix = [[False]*numRows for _ in range(math.ceil(len(s) / (2 * numRows - 2)) * (numRows - 1))]
        # 这儿尤其要注意的是多维列表与矩阵的区别，多维列表你可以用一个盒子套一个盒子来进行理解，有一个潜在的逻辑关系在里面
        # 比如说，你找到了第i个盒子才能在第i个盒子里找第j样东西，但矩阵不是，矩阵的行列是平等的
        # i代表列
        for i in range(math.ceil(len(s) / (2 * numRows - 2)) * (numRows - 1)):
            # j代表行
            for j in range(numRows):
                if (i % (numRows-1) == 0 or (i % (numRows-1)) == (numRows - 1 - j)) and s != '':
                    matrix[i][j] = s[0]
                    s = s[1:]
        return matrix


# a = Solution()
# print(a.convert("PAYPALISHIRING", 4))
# print(a.convert("PAYPALISHIRING", 3))
# print(a.convert("A", 1))
