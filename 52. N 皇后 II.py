# 对于这道题的思路，主要使用回溯的方法，对于每一行上的皇后，我在剩下的不同列中找到符合要求的皇后放置位置，然后整体采用暴力回溯方法进行求解。
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n: return []
        board = [['.'] * n for _ in range(n)]
        global res
        res = 0

        def isVaild(board, row, col):
            # 判断同一列是否冲突
            for i in range(len(board)):
                if board[i][col] == 'Q':
                    return False
            # 判断左上角是否冲突
            i = row - 1
            j = col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            # 判断右上角是否冲突
            i = row - 1
            j = col + 1
            while i >= 0 and j < len(board):
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            return True

        def backtracking(board, row, n):
            global res
            # 如果走到最后一行，说明已经找到一个解
            if row == n:
                res += 1
            for col in range(n):
                if not isVaild(board, row, col):
                    continue
                board[row][col] = 'Q'
                backtracking(board, row + 1, n)  # 每次都忘记这个公式，得好好记一下
                board[row][col] = '.'

        backtracking(board, 0, n)
        return res


solution = Solution()
print(solution.totalNQueens(3))
