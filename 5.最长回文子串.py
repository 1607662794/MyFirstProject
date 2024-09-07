class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 定义一个dp为二维数组，d[i][j]代表字符串s[i:j+1]是一个回文字符串，此时状态转移方程即为，如果s[i-1]==s[j+1]
        # 并且d[i][j]为True，那么新的字符串也为回文字符串。
        # 边界条件为一个必然是True，两个的话，需要两个相等则为True。
        # 最后从数学形式上来看，就是不断地沿着对角线去填充下三角矩阵
        # 从逻辑上来看，就是不断地去扩大子串来寻找最大子串。
        # length = len(s)
        # if length == 0:
        #     return None
        # else:
        #     max_len = 1
        #     max_str = s[0]
        #     dp = [[False] * length for i in range(length)]
        #     for i in range(length):
        #         dp[i][i] = True
        #         if i < length - 1 and s[i] == s[i+1]:
        #             dp[i][i+1] = True
        #             max_len = 2
        #             max_str = s[i:i+2]
        #     if length == 1 or length == 2:
        #         return max_str
        #
        #     for L in range(3,length+1):
        #         for i in range(length-L+1):
        #             if s[i] == s[L+i-1]:
        #                 dp[i][L+i-1] = dp[i+1][L+i-2]
        #             if dp[i][L+i-1] == True and L > max_len:
        #                 max_len = L
        #                 max_str = s[i:i+L]
        #     return max_str
        if len(s) <= 1:
            return len(s)
        max_length = 0
        dp = [[False] * len(s) for j in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            if i < len(s) - 1:
                if s[i] == s[i + 1]:
                    dp[i][i + 1] = True
                    max_length = 2
        for L in range(3, len(s)+1):
            for i in range(len(s)):
                j = L + i - 1
                if j >= len(s):
                    break
                dp[i][j] = dp[i + 1][j - 1] & (s[i] == s[j])
                if dp[i][j]:
                    max_length = max(max_length, L)
        return max_length
solution = Solution()
print(solution.longestPalindrome("ccc"))




