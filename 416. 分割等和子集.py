class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 0-1背包问题
        target = sum(nums)
        if target % 2 == 1: return False
        target //= 2
        dp = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            for j in range(target, nums[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])  # 对应不装入得情况，和装入的情况
        return target == dp[target]


solution = Solution()
print(solution.canPartition([2, 2, 1, 1]))
