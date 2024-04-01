class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp[i] : 以 i 结尾（一定包括 i）所能形成的最长上升子序列长度, 答案是 max(dp[i])，其中 i = 0,1,2, ..., n - 1，还是得找定义好的递归好的函数，这种方式是比较好些转移方程的。
        n = len(nums)
        if n == 0: return 0
        dp = [1] * n
        ans = 1
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    ans = max(ans, dp[i])
        return ans
