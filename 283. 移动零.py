# 我的思路是使用双指针，分别用于监督未检查的部分和检查过的部分。LeeCode的解法是直接交换，这样的话，操作步骤就会少一步，从而加速流程，它的也是双指针，指针之间存放的是零。
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        index = 0  # 从前往后开始检查元素为0的地方
        tail_index = 0  # 因为移动后的部分就不用检查了，肯定是0，所以需要有一个指针用于监管这部分
        while index < len(nums) - tail_index:
            if nums[index] == 0:
                nums.pop(index)
                nums.append(0)
                tail_index += 1
            else:
                index += 1
        return nums


solution = Solution()
print(solution.moveZeroes([0,0,1]))
