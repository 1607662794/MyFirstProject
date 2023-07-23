# 哈希表的应用
# 哈希表解法，创建一个空间为3的哈希表，分别用于检验横向，纵向和九宫格
class Solution(object):
    def compare(self, zone):
        war = []
        for a in range(3):
            for b in range(3):
                if (zone[a][b] != '.') and (zone[a][b] in war):
                    return False
                else:
                    war.append(zone[a][b])
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # 比较行
        for i in range(9):
            war = []
            for j in range(9):
                if (board[i][j] != '.') and (board[i][j] in war):
                    return False
                else:
                    war.append(board[i][j])
        # 比较列
        for i in range(9):
            war = []
            for j in range(9):
                if (board[j][i] != '.') and (board[j][i] in war):
                    return False
                else:
                    war.append(board[j][i])

        # 依次比较九个九宫格
        for i in range(3):
            for j in range(3):
                zone = []
                for obj in range(3):
                    zone.append(board[i*3+obj][j*3:j*3+3])
                if self.compare(zone) == False:
                    return False

        return True
        # 比较九宫格



board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", "8", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
a = Solution()
print(a.isValidSudoku(board))
# class HashNode:
#     def __init__(self,size = 3):
#         self.size = size
#         self.T = [[] for i in range(len(self.size))]
