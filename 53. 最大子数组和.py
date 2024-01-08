# 这道题我刚开始并没有思路，但是参考别人的.
# 妙呀，如果前面加起来都是负数，那我就不理他的，然后开始下一轮，把原来的nums【i】位置填充为前面的正数累加数，如果前面累加数是正的，那就继续加，负数就不加。那么不断记录就得出了最大累加数了，这样还可以节省开辟新的空间记录累加数结果。
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            nums[i] += max(nums[i - 1], 0)
        return max(nums)


solution = Solution()
print(solution.maxSubArray([2, -1, 3, -1, 1, -1, 5]))
