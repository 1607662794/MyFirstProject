# 我的思路是回溯，如果存在则返回True，不存在则返回False
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        def back_tracking(i, j, path):  # i,j表示当前网格的位置，path表示当前在网格中走过的位置
            if i < 0 or i > len(board) - 1 or j < 0 or j > len(board[0]) - 1 or (i, j) in path or board[i][j] != word[len(path)]:
                return False
            elif board[i][j] == word[len(path)] and len(path) + 1 == len(word):  # 因为不符合条件的也可能在里面，因此终止条件为：又发现一个相等值后，Word收集齐了。
                return True
            else:
                result = False
                path.append((i, j))
                if back_tracking(i, j - 1, path) or back_tracking(i - 1, j, path) or back_tracking(i, j + 1, path) or back_tracking(i + 1, j, path):
                    result = True
                path.remove((i, j))  # 记住每一个循环结束后，都需要将新走过的路径删除
                return result

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if back_tracking(i, j, []):  # 为了避免每次需要从路劲列表弹出定额数量元素的问题，使用形参来规避这种情况
                        return True  # 如果找到的话，直接返回True，否则的话，返回False
        return False


solution = Solution()
print(solution.exist([["F","E","S"],["D","E","E"]], "SEEEF"))
