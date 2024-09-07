class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        s = sorted(s)
        i = 1
        while i != len(s):
            if s[i] == s[i-1] and i == len(s)-1 or s[i] != s[i-1]:
                i += 1
            else:
                s.pop(i)
        return i

solution = Solution()
print(solution.lengthOfLongestSubstring("pwwkew"))
