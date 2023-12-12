# 对于这道题，我的思路是，因为题目所给的是一个非严格递增排列数组，所以新的元素应该是大于等于上一个元素
# 因此我在遍历这个列表时,出去刚开始的特例情况外，直接在参数引用的列表上操作，注意不要更改变量，否则会更换变量，也就是更换了变量的id
# 在pop的情况下，总数-1，在非pop的情况下，索引指针依次往前走
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        init_length = len(nums)
        if init_length == 0 or init_length == 1:
            return init_length
        length = 1
        while length < init_length:
            if nums[length] == nums[length - 1]:
                nums.pop(length)
                init_length -= 1
            else:
                length += 1
        return length


nums = [1,1]
solution = Solution()
print(solution.removeDuplicates(nums))
print(nums)
