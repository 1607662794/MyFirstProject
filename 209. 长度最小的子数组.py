class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # 华为滑动窗口
        length = len(nums) + 1
        sum = nums[0]
        head = 0
        tail = 0
        while tail < len(nums):
            if length == 1:
                return length
            if head < len(nums) and sum >= target and head <= tail:
                if tail - head + 1 < length:
                    length = tail - head + 1
                sum = sum - nums[head]  # 头要增加的话，删除的是本身
                head += 1
            else:
                tail += 1
                if tail < len(nums):
                    sum = sum + nums[tail]  # 尾要增加的话，增加的是新的尾巴
        if length > len(nums):
            return 0
        else:
            return length


solution = Solution()
print(solution.minSubArrayLen(target=4, nums=[1, 4, 4]))
