# 我的思路是，第一遍遍历，找到每种颜色的数量，第二遍遍历，在对应数量的位置上将列表元素更改过来即可。
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        red = 0
        white = 0
        blue = 0
        for _ in nums:
            if _ == 0:
                red += 1
            elif _ == 1:
                white += 1
            else:
                blue += 1
        for _ in range(red+white+blue):
            if _ <= red - 1:
                nums[_] = 0
            elif red <= _ <= red + white -1:
                nums[_] = 1
            else:
                nums[_] = 2
        return nums
solution = Solution()
print(solution.sortColors([2,0,2,1,1,0]))