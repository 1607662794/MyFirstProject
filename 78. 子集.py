# 我的思路是利用上一题的组合方式，给定所有子集的大小，将所有的情况选取一遍即可得到最终的结果。
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def combine(n, k):
            """
            :type n: int
            :type k: int
            :rtype: List[List[int]]
            """
            semi_arrays = []

            def backtrace(start_index):
                if len(semi_arrays) != k:
                    for _ in range(start_index, n + 1):
                        semi_arrays.append(nums[_ - 1])
                        backtrace(_ + 1)
                        semi_arrays.pop()
                else:
                    result.append(semi_arrays[:])  # 不切片的话，存进去的会是一个变量，而非数值
                    return

            backtrace(1)

        result = []

        for i in range(len(nums) + 1):
            combine(len(nums), i)
        return result


solution = Solution()
print(solution.subsets([1, 2, 3]))
