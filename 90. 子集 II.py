#利用之前的组合题目，因为我额外需要的代码为排除重复值
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        def combine(n, k):
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
        result.sort()
        i = 1
        while i < len(result):
            if result[i]==result[i-1]:
                result.pop(i)
                continue
            i += 1
        return result

solution = Solution()
print(solution.subsetsWithDup([2,1,2]))