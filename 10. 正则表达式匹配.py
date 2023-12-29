# 注意这道题有一个地方很容易出现理解上的偏差，*和前面的一个字符共同构成一个单位，可以有0个或者多个，而不是*单独作为一个独立的个体。
# 这道题真tm的做了一整天。
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        # 如果存在多个连续*号，则化整为一个，理解错啦，没有这种情况，因为是正则表达式
        i = 0
        new_p = ""
        while i < len(p):
            if i > 1 and p[i:i + 2] == p[i - 2:i]:#对于出现重复的a*，将多余的给删除
                i = i + 2
                continue
            if i < len(p) - 1 and p[i] == '*' and p[i + 1] == '*':#对于出现重复的*，将多余的给删除
                i = i + 1
                continue
            new_p += p[i]
            i += 1
        return self.dfs(s, new_p)

    def total_number(self, p):  # 统计p中非*的字符数量
        index = 0
        number = len(p)
        while index < len(p):
            if p[index] == "*":
                number -= 2
            index += 1
        return number

    def dfs(self, s, p):

        # 统计p中非*的字符数量
        number = self.total_number(p)

        # 初步排除，在没有*的情况下，如果s与p的数量不对，那么必然返回False
        if '*' not in p and len(s) != len(p):
            return False

        elif len(p) > 1 and p[1] == '*':  # 不用考虑那么多的情况，将*从0到最大长度整体循环一遍就可以得到
            # dfs = [False for _ in range(len(s) + 1 - number)]
            for i in range(len(s) + 1 - number):
                if len(p) == 2:
                    end_list = "".join([p[0] for _ in range(i)])
                else:
                    end_list = "".join([p[0] for _ in range(i)]) + p[2:]
                # dfs[i] = self.dfs(s, end_list)
                # if dfs[i] == True:
                if self.dfs(s, end_list) == True:
                    return True
            return False

        elif s == '' and p != '' or s != "" and p == '':  # 迭代的判别条件:不匹配
            return False

        elif s == '' and p == '':  # 迭代的判别条件:匹配
            return True

        elif s[0] != p[0] and p[0] != '.':  # 普通字符不相匹配的情况
            return False

        elif s[0] == p[0] or p[0] == '.':  # 普通字符相匹配的情况
            return self.dfs(s[1:], p[1:])


solution = Solution()
print(solution.isMatch("a", "ab*"))
