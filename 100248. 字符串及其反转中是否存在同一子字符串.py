class Solution(object):
    def isSubstringPresent(self, s):
        """
        :type s: str
        :rtype: bool
        """
        reversed_s = "".join(reversed(s))
        for i in range(len(s)-1):
            if s[i:i+2] in reversed_s:
                return True
        return False

solution = Solution()
print(solution.isSubstringPresent("leetcode"))