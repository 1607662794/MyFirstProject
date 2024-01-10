# 将45题改一下，我的思路是使劲往前跳跃，能够跳跃的最远距离为max，如果有一次发现最远距离max等于当前值了，便证明跳跃卡住了，此时，如果到达了末尾还好，没有到达末尾的话，那就是卡住了。
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True
        elif len(nums) > 1 and nums[0] == 0:
            return False
        else:
            max = 0
            max_index = 0
            current_index = 0
            while current_index < len(nums):  # 开头不为零的情况
                for i in range(1, nums[current_index] + 1):  # 起码得跳跃一次，计算下一次跳跃范围内，最远跳跃距离
                    if current_index + i + nums[current_index + i] >= max:  # 这个等于号很重要，一直转移到极大值处
                        max = current_index + i + nums[current_index + i]
                        max_index = current_index + i
                        if max_index + nums[current_index + i] >= len(nums) - 1:
                            return True
                if nums[max_index] == 0:  # 如果极大值为0，则表明移动不了
                    return False
                current_index = max_index


solution = Solution()
print(solution.canJump([1, 1, 2, 2, 0, 1, 1]))
