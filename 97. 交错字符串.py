# 我的思路是，建立两个指针，分别用于遍历前两个字符串，如果遇到两个都可以选择的情况，那么通过or来实现两种策略的选择！
# 然而这种方法没有剪枝，时间超限了！,将其等效为一个二维矩阵迷宫，你会发现，不同的走法可能会在后期相遇，因此采用的方法应该是动态规划。
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """

        # def backtracking(index_1, index_2, index_3):
        #     if index_1 == len(s1) and index_2 == len(s2):  # 前两个是回溯法中的终止条件
        #         return True
        #     elif index_1 > len(s1) or index_2 > len(s2):
        #         return False
        #     elif index_2 == len(s2) and index_1 != len(s1) and s1[index_1] == s3[index_3]:
        #         return backtracking(index_1 + 1, index_2, index_3 + 1)
        #     elif index_1 == len(s1) and index_2 != len(s2) and s2[index_2] == s3[index_3]:
        #         return backtracking(index_1, index_2 + 1, index_3 + 1)
        #     elif index_1 < len(s1) and index_2 < len(s2) and s1[index_1] == s3[index_3] and s2[index_2] != s3[index_3]:  # 后边这一串是选择列表
        #         return backtracking(index_1 + 1, index_2, index_3 + 1)
        #     elif index_1 < len(s1) and index_2 < len(s2) and s1[index_1] != s3[index_3] and s2[index_2] == s3[index_3]:
        #         return backtracking(index_1, index_2 + 1, index_3 + 1)
        #     elif index_1 < len(s1) and index_2 < len(s2) and s1[index_1] == s3[index_3] and s2[index_2] == s3[index_3]:
        #         return backtracking(index_1 + 1, index_2, index_3 + 1) or backtracking(index_1, index_2 + 1,
        #                                                                                index_3 + 1)
        #     else:
        #         return False  # 对应的情况，前两个字符串的当前字符都对不上号 s1[index_1] != s3[index_3] and s2[index_2] != s3[index_3]
        #
        # if len(s1) + len(s2) != len(s3):
        #     return False
        # elif s1 == "" and s2 != s3:
        #     return False
        # elif s2 == "" and s1 != s3:
        #     return False
        # else:
        #     return backtracking(0, 0, 0)

        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)
        if (len1 + len2 != len3):
            return False
        dp = [[False] * (len2 + 1) for i in range(len1 + 1)]
        dp[0][0] = True
        for i in range(1, len1 + 1):
            dp[i][0] = (dp[i - 1][0] and s1[i - 1] == s3[i - 1])
        for i in range(1, len2 + 1):
            dp[0][i] = (dp[0][i - 1] and s2[i - 1] == s3[i - 1])
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                dp[i][j] = (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]) or (
                            dp[i - 1][j] and s1[i - 1] == s3[i + j - 1])
        return dp[-1][-1]



solution = Solution()
print(solution.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
