class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 注意这道题最终的结果是原地操作，因此其他操作在LeeCode中其实并不能加载出来。
        # 方法一：利用栈的思想，弹出一个，压进去一个
        # for i in range(k):
        #     nums.insert(0,nums.pop())
        # return nums
        #方法二：使用reverse函数，翻转两遍
        k = k % len(nums)
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
        return nums
solution = Solution()
print(solution.rotate(nums = [1,2,3,4,5,6,7], k = 3))