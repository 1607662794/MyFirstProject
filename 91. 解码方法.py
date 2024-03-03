# 我的思路是使用回溯，但是这样的话，时间会超限，LeeCode使用动态规划，从后往前找，用空间换时间
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        def backtracking(head, tail):
            if head == tail + 1:
                return 1
            elif head > tail + 1 or s[head] == '0':# 特殊情况,前一步是两步跳的时候，直接跳到了0处
                return 0
            elif tail - head >= 1 and s[head+1] == '0':  # 特殊情况
                return backtracking(head + 2, tail)
            elif tail - head >= 1 and int(s[head:head + 2]) <= 26:
                return backtracking(head + 2, tail) + backtracking(head + 1, tail)
            else:
                return backtracking(head + 1, tail)

        return backtracking(0, len(s) - 1)


solution = Solution()
print(solution.numDecodings("2101"))
