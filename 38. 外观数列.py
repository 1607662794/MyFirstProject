# 首先观察这个题目的特点，1.插入一个数字，输出它的字符串2.除了第一个数，其余全是偶数个3.最多三个相同数字连在一起4.但是末尾最多只有两个数字是相同的。
# 我的思路是使用回溯，但是并不将截止条件放在一个函数中，而是分开，因为s在回溯的过程中一直处于变化的过程中，在对s不停地进行操作，不像常数一样。
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        while n - 1 > 0:
            s = self.appearance_sequence(s)
            n = n - 1
        return s

    def appearance_sequence(self, s):  # 描述前一项，
        i = 0
        new_s = ''
        while i < len(s) - 1:  #
            if s[i] != s[i + 1]:
                new_s = new_s + '1' + s[i]
                i += 1
            elif i + 2 <= len(s) - 1 and s[i] == s[i + 2]:
                new_s = new_s + "3" + s[i]
                i += 3
            else:
                new_s = new_s + "2" + s[i]
                i += 2
        if i == len(s) - 1:
            new_s = new_s + '1' + s[i]
        return new_s


solution = Solution()
print(solution.countAndSay(6))
