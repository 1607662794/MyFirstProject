class Solution(object):
    """时间复杂度：O(N^2);空间复杂度：O(1)"""
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


class Solution:
    """官方说是哈希表，其实就是字典"""
    '''时间复杂度：O(N)；空间复杂度：O(N)'''
    def twoSum(self, nums, target):
        hashtable = dict()
        print(hashtable)
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []


'''测试'''
nums = [2, 7, 11, 15]
target = 9
a = Solution()
print(a.twoSum(nums, target))
