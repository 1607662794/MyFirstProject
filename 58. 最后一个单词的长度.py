# 我的思路是从后往前依次寻找
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '' or s == ' ':
            return 0
        else:
            length = 0
            for i in range(len(s) - 1, -1, -1):
                if s[i] == ' ' and length == 0:  # 避免刚开始的几个空格干扰的情况
                    continue
                elif s[i] == ' ':  # 最后一个单词统计结束
                    return length
                else:
                    length += 1
            return length  # 处理剩余的边界条件


solution = Solution()
print(solution.lengthOfLastWord("Hello World"))
