class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # max_multipy用来存储以i结尾的乘积最大子数组的乘积,空间换时间，自底向上
        # 最小值乘一个负数，则可能成为最大值。
        # 最大值乘一个正数，则可能成为最大值。
        n = len(nums)
        max__dp = [1] * (n + 1)
        min_dp = [1] * (n + 1)
        ans = float('-inf')

        for i in range(1, n + 1):
            max__dp[i] = max(max__dp[i - 1] * nums[i - 1],
                             min_dp[i - 1] * nums[i - 1], nums[i - 1])  # 如果遇上不连续的情况，就是选择本身为最大值
            min_dp[i] = min(max__dp[i - 1] * nums[i - 1],
                            min_dp[i - 1] * nums[i - 1], nums[i - 1])
            ans = max(ans, max__dp[i])
        return ans


solution = Solution()
print(solution.maxProduct([2, 3, -2, 4]))
