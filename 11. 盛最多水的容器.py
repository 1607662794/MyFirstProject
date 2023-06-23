class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        '''一个新的思路，双重循环解决，但是超时版'''
        max_area = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                if min(height[i], height[j]) * (j - i) > max_area:
                    max_area = min(height[i], height[j]) * (j - i)
        return max_area
a = Solution()
print(a.maxArea([1,8,6,2,5,4,8,3,7]))