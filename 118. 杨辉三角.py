class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []

        def dp(number):
            if number > numRows:
                return result
            else:
                row = []
                for i in range(number):  # 其实这儿可以优化的，因为有对称关系，虽然最后省不了多少时间
                    if i == 0:
                        row.append(1)
                    elif i == number - 1:
                        row.append(1)
                    else:
                        row.append(result[-1][i - 1] + result[-1][i])
                result.append(row)
                dp(number + 1)

        dp(1)
        return result


solution = Solution()
print(solution.generate(4))
