# 对于，这道题的思路，采用二次幂的对数操作，整体只用迭代的方式，终点为次方幂等于1.
# 这道题有一个地方值得注意的是，**会引发OverflowError，而乘法不会，这可能在 Python 诞生之初就被深深地埋藏在历史的迷雾中了。Python 中的浮点乘法必须遵循 IEEE-754 标准制定的规则，即乘法溢出到特殊值 float('inf')。
# 但由于现在已不清楚的原因，设计 Python 的指数运算符和 pow() 函数的人做出了一个不同的决定，即引发 OverflowError。
# 这种差异背后可能没有真正的逻辑。可能只是有人当时觉得这是个好主意。
# 顺便说一句，内置指数运算符 **、pow() 内置函数和 math.pow 函数都会将 2.0 的幂次（负巨数）舍入为 0.0。
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        if n == 0:
            return 1
        elif n < 0:
            return 1.0 / self.myPow(x, -n)
        else:
            return self.power(x, n)

    def power(self, x, n):
        # 进行幂次方的操作
        if n == 1:
            return float(x)
        elif n % 2 != 0:
            return self.power(x, n // 2) ** 2 * x
        else:
            return self.power(x, n // 2) ** 2


solution = Solution()
print(solution.myPow(2.00000, -2147483648))
