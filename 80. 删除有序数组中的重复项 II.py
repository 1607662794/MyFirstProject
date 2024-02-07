# 我的思路是，既然列表本身是有序的，那么完全可以根据它的有序性，遍历列表进行寻找。
# Leecode中很多方法是采用的双指针操作。
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        else:
            i = 2
            while i <= len(nums) - 1:
                if nums[i] == nums[i-1] and nums[i-1] == nums[i-2]:
                    nums.pop(i)
                else:
                    i = i + 1
            return len(nums)


solution = Solution()
print(solution.removeDuplicates([1,1,1]))