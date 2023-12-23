# 我的思路是，对于一个target，首先和数组最后一个值进行对比，如果大于最后一个值，则从前往后找，如果小于最后一个值，则从后往前找，最后的时间复杂度应该为log n
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums == []:
            return -1
        if target == nums[-1]:
            return len(nums) - 1
        elif target > nums[-1]:
            for _ in range(len(nums)):
                if target == nums[_]:
                    return _
            return -1
        else:
            for _ in range(len(nums)):
                if target == nums[len(nums) - 1 - _]:
                    return len(nums) - 1 - _
            return -1

solution = Solution()
print(solution.search([4,5,6,7,0,1,2],0))
