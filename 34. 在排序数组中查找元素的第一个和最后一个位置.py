# 对于这道题，我的思路是首先编写一下二分法查找的函数，只要找到一个target值对应的索引就可以，然后以这个索引为基点，向左右两边进行扩展
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index = self.search(nums, target, 0, len(nums) - 1)
        if index == -1:  # 该目标值不存在于数组中
            return [-1, -1]
        else:
            left = 1
            right = 1
            while right + index <= len(nums) - 1 and nums[index + right] == target:
                right = right + 1
            while index - left >= 0 and nums[index - left] == target:
                left = left + 1
            return [index - left + 1, index + right - 1]

    def search(self, nums, target, l, r):  # 二分法搜索
        if r == -1 or (r - l) == 0 and nums[l] != target or (r - l) == 1 and nums[l] > target:  # 最后的情况要么是两个要么是一个
            return -1
        elif nums[(l + r) // 2] < target:
            return self.search(nums, target, l=(l + r) // 2 + 1, r=r)
        elif nums[(l + r) // 2] > target:
            return self.search(nums, target, l=l, r=(l + r) // 2 - 1)
        else:
            return (l + r) // 2


solution = Solution()
print(solution.searchRange([2, 2], 2))
