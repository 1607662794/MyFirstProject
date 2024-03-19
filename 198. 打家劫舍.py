class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

            # 子问题：
            # f(k) = 偷 [0..k) 房间中的最大金额k 个房子中最后一个房子是 Hk−1H_{k-1}H
            # k−1
            # ​
            #  。如果不偷这个房子，那么问题就变成在前 k−1k-1k−1 个房子中偷到最大的金额，也就是子问题 f(k−1)f(k-1)f(k−1)。如果偷这个房子，那么前一个房子 Hk−2H_{k-2}H
            # k−2
            # ​
            #   显然不能偷，其他房子不受影响。那么问题就变成在前 k−2k-2k−2 个房子中偷到的最大的金额。两种情况中，选择金额较大的一种结果。

            # f(0) = 0
            # f(1) = nums[0]
            # f(k) = max{ rob(k-1), nums[k-1] + rob(k-2) }

        N = len(nums)
        dp = [0] * (N + 1)
        dp[0] = 0
        dp[1] = nums[0]
        for k in range(2, N + 1):
            dp[k] = max(dp[k - 1], nums[k - 1] + dp[k - 2])
        return dp[N]



solution = Solution()
print(solution.rob([1,2,3,1]))
