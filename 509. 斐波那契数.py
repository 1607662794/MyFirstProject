class Solution(object):

    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 华为递归解法，但是太耗时了，可以加一个列表来进行存储，以空间换时间。
        if n == 1 or n == 0:
            return n
        else:
            result = [0 for i in range(n + 1)]
            result[1] = 1
            for i in range(2, n + 1):
                result[i] = result[i - 1] + result[i - 2]
            return result[n]
solution = Solution()
print(solution.fib(0))
