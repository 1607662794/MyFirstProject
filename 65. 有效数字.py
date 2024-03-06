# 我的思想是分而划之，不断地根据条件将目标划分成确定类别的判断。
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def integers(i, j):  # 用于判断i,j之间的字符串是否满足整数部分的要求
            if (s[i] == "+" or s[i] == "-") and i == j:
                return False
            elif s[i] == "+" or s[i] == "-":  # 如果开头是正负号，那么检查从正负号后开始
                for k in range(i + 1, j + 1):
                    if 48 > ord(s[k]) or ord(s[k]) > 57:
                        return False
                return True
            else:  # 如果开头不是正负号，那么检查从头开始
                for k in range(i, j + 1):
                    if 48 > ord(s[k]) or ord(s[k]) > 57:
                        return False
                return True

        def radix(i, j):  # 用于判断i,j之间的字符串是否满足前半部分的要求
            if s.count(".") > 1:  # 用是否包含"."来判断该部分是整数还是小数
                return False
            elif s.count(".") == 1:  # 该情况对应此部分字符串为小数
                if (s[i] == "+" or s[i] == "-") and i + 1 >= j or i == j:
                    return False
                elif s[i] == "+" or s[i] == "-":  # 如果开头是正负号，那么检查从正负号后开始
                    for k in range(i + 1, j + 1):
                        if 46 > ord(s[k]) or ord(s[k]) > 57 or ord(s[k]) == 47:
                            return False
                    return True
                else:  # 如果开头不是正负号，那么检查从头开始
                    for k in range(i, j + 1):
                        if 46 > ord(s[k]) or ord(s[k]) > 57 or ord(s[k]) == 47:
                            return False
                    return True
            else:
                return integers(i, j)

        if s.count("e") + s.count("E") > 1:  # e部分过多
            return False
        elif s.count("e") + s.count("E") == 0:  # 只有前半部分
            return radix(0, len(s) - 1)
        else:  # 存在整数和小数的两部分
            if s.count("e") == 1:
                index = s.index("e")
            else:
                index = s.index("E")
            if index == 0 or index == len(s) - 1:
                return False
            else:
                return radix(0, index - 1) and integers(index + 1, len(s) - 1)

solution = Solution()
print(solution.isNumber("inf"))
