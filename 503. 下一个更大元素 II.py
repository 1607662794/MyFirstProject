class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #华为单调栈
        # 建立「单调递减栈」，并对原数组遍历一次：
        #
        # 如果栈为空，则把当前元素放入栈内；
        # 如果栈不为空，则需要判断当前元素和栈顶元素的大小：
        # 如果当前元素比栈顶元素大：说明当前元素是前面一些元素的「下一个更大元素」，则逐个弹出栈顶元素，直到当前元素比栈顶元素小为止。
        # 如果当前元素比栈顶元素小：说明当前元素的「下一个更大元素」与栈顶元素相同，则把当前元素入栈。

        N = len(nums)
        res = [-1] * N
        stack = []
        for i in range(N * 2):
            while stack and nums[stack[-1]] < nums[i % N]:
                res[stack.pop()] = nums[i % N]
            stack.append(i % N)
        return res