# 这道题的思路是使用排列与组合，先选出需要几个一步走，需要几个两步走，然后进行组合。
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        compose = {}
        result = 0
        for i in range(n + 1):
            if (n - i) % 2 == 0:
                compose[i] = (n - i) // 2
            else:
                continue

        def array(i, j):
            molecule = 1
            for _ in range(i + j):
                molecule *= (_ + 1)
            denominator = 1
            for _ in range(i):
                denominator *= (_ + 1)
            for _ in range(j):
                denominator *= (_ + 1)
            return molecule / denominator

        for i, j in compose.items():
            result = result + array(i, j)
        return int(result)


solution = Solution()
print(solution.climbStairs(2))
