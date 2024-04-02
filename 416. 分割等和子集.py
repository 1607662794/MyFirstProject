class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 将这个问题转换为0-1背包问题
        if sum(nums) % 2 != 0:
            return False
        else:
            target = sum(nums) // 2
            result = [[0 for i in range(target + 1)] for j in range(len(nums) + 1)]
            for i in range(1, len(nums) + 1):
                for j in range(1, target + 1):
                    if j >= nums[i-1]:
                        result[i][j] = max(result[i - 1][j], nums[i-1] + result[i - 1][j - nums[i-1]])  # 取最大值即塞满的情况
                        if result[i][j] == target:
                            return True
                    else:
                        result[i][j] = result[i - 1][j]
            return False




solution = Solution()
print(solution.canPartition([1,5,10,6]))
