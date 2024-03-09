# 我的方法是利用sorted函数，但是这道题可以用哈希求解，虽然LeeCode官方的题解，我没有看出来哈希体现在哪个地方？
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 方法一：使用内置函数进行求解，有点儿偏向于暴力求解的样子
        # if len(nums) <= 1:
        #     return len(nums)
        # nums = sorted(nums)
        # max_length = 1
        # length = 1
        # for i in range(1, len(nums)):
        #     if nums[i - 1] == nums[i]:
        #         continue
        #     elif nums[i - 1] == nums[i] - 1:
        #         length += 1
        #     else:
        #         length = 1
        #     if length > max_length:
        #         max_length = length
        # return max_length

        # 方法二：使用哈希进行求解
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak


solution = Solution()
print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))
