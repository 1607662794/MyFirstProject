# 我的思路是，首先判断该在k的左边还是右边进行寻找，此时的子集是有序的，因此可以采用二分法进行寻找。
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

        def binary(head, tail, nums):  # 二分法
            if head == tail and nums[head] != target or head == tail - 1 and nums[head] != target and nums[
                tail] != target:  # 后边的一种情况是为了避免陷入无限循环
                return False
            elif nums[(head + tail) // 2] == target or head == tail - 1 and nums[head] == target or head == tail - 1 and \
                    nums[tail] == target:  # 后边的一种情况是为了避免陷入无限循环
                return True
            elif nums[(head + tail) // 2] >= target:
                return binary(head, (head + tail) // 2, nums)
            else:
                return binary((head + tail) // 2, tail, nums)

        if len(nums) == 0 or len(nums) == 1 and nums[0] != target:  # 对应列表极短的两种情况
            return False
        elif nums[0] == target:
            return True
        k = len(nums) - 1
        for i in range(1, len(nums)):  # 寻找k的具体数值
            if nums[i] < nums[i - 1]:
                k = i - 1
                break
        if nums[0] == target:
            return True
        elif nums[0] < target:
            return binary(0, k, nums)
        else:
            if k == len(nums) - 1:
                return binary(k, len(nums) - 1, nums)  # 如果没有进行翻转，则特殊情况特殊考虑，因为加1后会超出列表范围
            else:
                return binary(k + 1, len(nums) - 1, nums)


solution = Solution()
print(solution.search([1, 3], 0))
