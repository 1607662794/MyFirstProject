# 计划采用回溯法进行全排列的组合,回溯法就是带了剪枝操作的深度优先搜索。
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(x):
            if x == len(nums) - 1:
                res.append(list(nums))  # 添加排列方案
                return
            for i in range(x, len(nums)):#此时固定了x-1位数，其余的分别放在x位上一次，这样就形成了全排列。
                nums[i], nums[x] = nums[x], nums[i]  # 交换，将 nums[i] 固定在第 x 位
                dfs(x + 1)  # 开启固定第 x + 1 位元素
                nums[i], nums[x] = nums[x], nums[i]  # 恢复交换

        res = []
        dfs(0)
        return res

solution = Solution()
print(solution.permute([1, 2, 3]))
