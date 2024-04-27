class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 快慢指针，只要有重复值，那么一定会有闭环，至于为什么第二次一定会在入口处相遇可见力扣公式推导。
        slow_index = 0
        quick_index = 0
        while True:
            if slow_index % len(nums) != quick_index % len(nums) and nums[slow_index % len(nums)] == nums[
                quick_index % len(nums)]:
                return nums[slow_index % len(nums)]
            else:
                slow_index += 1
                quick_index += 2
                continue


solution = Solution()
print(solution.findDuplicate([3, 1, 3, 4, 2]))
