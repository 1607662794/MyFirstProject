class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        '''一个新的思路，双重循环解决，但是超时版'''
        # max_area = 0
        # for i in range(len(height)):
        #     for j in range(i + 1, len(height)):
        #         if min(height[i], height[j]) * (j - i) > max_area:
        #             max_area = min(height[i], height[j]) * (j - i)
        # return max_area
        '''借鉴别人的思路，两个指针分别位于列表两侧，通过不断向内行走，寻找面积最大值；当前的两边，更改大边肯定无用，因为面积不是有它控制的，只能更改小边，就是多元函数的思想'''
        max_area = 0
        i = 0
        j = len(height) - 1
        while i != j:
            if min(height[i], height[j]) * (j - i) > max_area:
                max_area = min(height[i], height[j]) * (j - i)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area


a = Solution()
print(a.maxArea([2, 3, 4, 5, 18, 17, 6]))
