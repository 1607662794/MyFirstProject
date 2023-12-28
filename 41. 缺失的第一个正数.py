# 参考别人的思路是这样的，将1-len(nums)分别进行摆放，摆放到他们对应的位置上，然后和一个同样长度的数组进行对比，该数组是以1开头的递增数列，也即与标准值进行对比，从而得到最终的结果。
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):  # 将不符合的数字移动到合适的位置上，非范围内的正整数肯定不用动，没有数值大小的意义，然后整体上来看，时间复杂度刚好是过了一年数组的样子。
            if 1 <= nums[i] and nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:
                self.swap(nums, i, nums[i] - 1)
            else:
                i += 1
        i = 0
        while i < len(nums):  # 与标准值做对比
            if nums[i] != i + 1:
                return i + 1
            else:
                i += 1
        return i + 1

    def swap(self, nums, index_1, index_2):
        nums[index_1], nums[index_2] = nums[index_2], nums[index_1]


solution = Solution()
print(solution.firstMissingPositive([3, 4, -1, 1]))
