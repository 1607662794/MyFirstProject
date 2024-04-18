class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 1:
            return 0
        else:
            sum_left = 0
            sum_right = sum(nums[1:])
            if sum_right == sum_left:
                return 0
            for i in range(1,length):
                sum_left = sum_left + nums[i-1]
                sum_right = sum_right - nums[i]
                if sum_right == sum_left:
                    return i
            return -1


solution = Solution()
print(solution.pivotIndex([2,1,-1]))