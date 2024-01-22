# 这道题主要使用二分的思想，对于有顺序的寻找而言，直接通过二分的方式能够节省很多时间
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        def binary_search(init, end, mid):
            if mid ** 2 <= x and (mid + 1)**2 > x:
                return mid
            elif mid ** 2 < x:
                return binary_search(mid + 1, end, (mid + 1 + end) // 2)
            else:
                return binary_search(init, mid - 1, (init + mid - 1) // 2)

        return binary_search(1, x, (1 + x) // 2)

solution = Solution()
print(solution.mySqrt(8))
