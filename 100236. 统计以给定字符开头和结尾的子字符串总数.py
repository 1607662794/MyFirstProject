class Solution(object):
    def countSubstrings(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: int
        """
        # 我的思路是使用数学方法，因为c之间的字符其实并没有什么影响
        sum = 0
        num = 0
        for i in range(len(s)):
            if s[i] == c:
                num += 1
        for i in range(1, num + 1):
            sum = sum + i
        return sum


solution = Solution()
print(solution.countSubstrings(s="abada", c="a"))
