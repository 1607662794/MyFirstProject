# 对于这道题，我的思路是，首先，从后往前，两两对比进行判断，如果后一个大于前一个的话，将后一个插入后边的列表中，然后将插入位置前一个的数值放在开头，最后整体进行翻转。
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        b = len(nums) - 1
        reverse_num = len(nums) // 2
        if b == 0 or b == -1:
            return nums

        while nums[b - 1] >= nums[b] and b >= 1:  # 从后往前找，要是逐渐增大，则不用进行转换，如果不是则需要对找到的部分进行调整
            b -= 1

        if b == 0:  # 如果遇到终点，则整个列表进行翻转
            for _ in range(reverse_num):
                value = nums[_]
                nums[_] = nums[len(nums) - 1 - _]
                nums[len(nums) - 1 - _] = value
        elif b == len(nums)-1:  #对于直接可以修改的直接修改
            value_1 = nums[b]
            nums[b] = nums[b-1]
            nums[b-1] = value_1
        else:# 对找到的部分进行排序,次大的一个数放在开头，然后最新的一个数插入,插入后进行整体翻转
            value_1 = nums[b - 1]
            index = b + 1
            while index <= len(nums) - 1 and value_1 < nums[index]:
                index += 1
            value_2 = nums[index-1]
            nums[b-1] = value_2
            nums[index-1] = value_1
            reverse_num = (len(nums)-b)//2
            for _ in range(reverse_num):
                value = nums[b+_]
                nums[b+_] = nums[len(nums) - 1 - _]
                nums[len(nums) - 1 - _] = value
        return nums

solution = Solution()
print(solution.nextPermutation([5,4,7,5,3,2]))
