#我的思路是递归，对于n=1而言，有00和01两种结果；
# 对于n=2而言，控制第一位变换一次，n=1的结果镜像一次，便可得到n=2的结果：00,01,11,10；
# 对于n=3而言，控制第一位变换一次，n=2的结果镜像一次，便可得到n=2的结果：000,001,011,010,110,111,101,100；
# 然后观察十进制数也有相同规律
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        def backtrace(n):
            if n == 1:
                return [0,1]
            else:
                n = n-1
                result = backtrace(n)
                for i in range(len(result)):
                    result.append(2 ** n + result[-i*2-1])
                return result

        return backtrace(n)
solution = Solution()
print(solution.grayCode(3))

