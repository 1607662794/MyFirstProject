# 我的思路是回溯，如果存在则返回True，不存在则返回False
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        def back_tracking(i, j, k):  # i,j表示当前网格的位置，k当前对象位于单词中的位置
            if k == len(word):
                return True
            elif i < 0 or i > len(board) - 1 or j < 0 or j > len(board[0]) - 1 or (i, j) in path:
                return False
            elif board[i][j] == word[k]:
                path.append((i, j))
                k += 1

            if back_tracking(i, j - 1, k + 1):
                path.pop
                back_tracking(i - 1, j, k + 1)
                back_tracking(i, j + 1, k + 1)
                back_tracking( i + 1, j, k + 1)

        for i in range(len(board)):
            for j in range(len(board[0])):
                path = [] #每一次进行寻找时，都需要重置保存路径
                if board[i][j] == word[0]:
                    if back_tracking(i, j, 0):
                        return True  # 如果找到的话，直接返回True，否则的话，返回False

        return False
