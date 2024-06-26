class Solution(object):
    # 环装结构用列表切片来替代。
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            return max(self.rob1(nums[1:]), self.rob1(nums[:-1]))

    def rob1(self, nums):
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            dp = [0 for i in range(len(nums))]
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
            return dp[-1]
solution = Solution()
print(solution.rob([1,2,3,1]))