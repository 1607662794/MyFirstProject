class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) <= k:
            return len(nums)
        max_length = k
        current_length = 0
        zero_num = 0
        head = 0
        tail = k - 1
        while tail < len(nums):
            if nums[head] == 0 and zero_num <= k:
                zero_num += 1
                head += 1
                current_length += 1
                if current_length > max_length:
                    max_length = current_length
            elif nums[head] == 0 and zero_num > k:
                tail = head
