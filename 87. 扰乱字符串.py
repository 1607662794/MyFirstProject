# 暴力解法，通过使用回溯，但是通过调用cache貌似可以将时间效率提上去，总体上还是暴力解法。
class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        # 方法一：暴力解法
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False

        for i in range(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]) or (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])):
                return True
        return False

