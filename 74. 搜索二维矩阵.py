# 我的思路是将二维二分法转换到一维二分法的思路上，然后再转换回二维上。
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def binary_search(head,tail,mid):
            if target == matrix[mid[0]][mid[1]]:#中间值等于目标值的情况
                return True
            if head == mid and matrix[mid[0]][mid[1]] != target:#对于经过运算后，首尾没有找到的情况,中间值最多只能与头部值相等。
                return False
            elif target < matrix[mid[0]][mid[1]]:
                return binary_search(head,mid,[(head[0]*len(matrix[0])+head[1] + mid[0]*len(matrix[0])+mid[1])//2//len(matrix[0]),((head[0]*len(matrix[0])+head[1] + mid[0]*len(matrix[0])+mid[1])//2)%len(matrix[0])])
            else:
                return binary_search(mid, tail, [(tail[0]*len(matrix[0])+tail[1] + mid[0]*len(matrix[0])+mid[1]) // 2 // len(matrix[0]),((tail[0]*len(matrix[0])+tail[1] + mid[0]*len(matrix[0])+mid[1]) // 2) % len(matrix[0])])

        if len(matrix) == 0:
            return False
        else:
            if target == matrix[0][0] or target == matrix[len(matrix)-1][len(matrix[0])-1]:#对于初始情况的边缘处直接相等的情况
                return True
            return binary_search([0,0],[len(matrix)-1,len(matrix[0])-1],[((len(matrix) * len(matrix[0]) - 1) // 2) // len(matrix[0]), ((len(matrix) * len(matrix[0]) - 1) // 2) % len(matrix[0])])

solution = Solution()
print(solution.searchMatrix([[1,3]],3))
