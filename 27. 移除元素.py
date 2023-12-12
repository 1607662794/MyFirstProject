#整体思路和上一道题基本上是一致的，我使用两个指针，一个控制当前检测位置，一个控制整体长度，采用pop函数进行删除
#力扣上的双指针大法主要使用移动的方法，一个指针指向当前确定好的位置，另一个从前往后遍历，一快一慢两个指针进行工作。
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        index = 0
        while index < length:
            if nums[index] == val:
                nums.pop(index)
                length -= 1
            else:
                index += 1
        return index

nums = [3,2,2,3]
val = 3
solution = Solution()
print(solution.removeElement(nums,val))
print(nums)
