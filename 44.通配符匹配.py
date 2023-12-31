# 和第十题很像，参考第十题动态规划的思路。反而和我刚开始理解错误的解题思路比较相似：?可以单独出现。
# 我使用的方法为回溯，观察到f[i - 1][j] 与 f[i][j] 中的 f[i][j - 1] 开始的后半部分是一样的，其实也就是可以使用动态规划。
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        # 如果存在多个连续*号，则化整为一个。只在第一遍的时候执行。
        i = 0
        while i < len(p):
            if i < len(p) - 1 and p[i] == '*' and p[i + 1] == '*':  # 对于出现重复的*，将多余的给删除
                p = p[0:i] + p[i + 1:]
                continue
            i += 1
        return self.dfs(s, p)

    def total_number(self, p):  # 统计p中非*的字符数量。每次迭代都需要执行。
        i = 0
        number = len(p)
        while i < len(p):
            if p[i] == "*":
                number -= 1
            i += 1
        return number

    def dfs(self, s, p):
        number = self.total_number(p)
        if '*' not in p and len(s) != number or '*' in p and len(s) < number:  # 初步排除，在没有*的情况下，如果s与p的数量不对，那么必然返回False
            return False

        elif s == '' and p == '':  # 迭代的判别条件:匹配
            return True
        # 为了提高计算效率，首先从两边开始往中间收一收，如果只是从前往后的话，倒是可以把下边这段代码放在*判断后边。
        elif p[0] != '*' and len(s) > 0 and len(p) > 0 and s[0] != p[0] and p[0] != '?':  # 普通字符相匹配的情况
            return False

        elif p[-1] != '*' and len(s) > 0 and len(p) > 0 and s[-1] != p[-1] and p[-1] != '?':  # 普通字符相匹配的情况
            return False

        elif p[0] != '*' and len(s) > 0 and len(p) > 0 and (s[0] == p[0] or p[0] == '?'):  # 普通字符相匹配的情况
            return self.dfs(s[1:], p[1:])

        elif p[-1] != '*' and len(s) > 0 and len(p) > 0 and (s[-1] == p[-1] or p[-1] == "?"):  # 普通字符相匹配的情况
            return self.dfs(s[0:-1], p[0:-1])

        elif p[0] == '*':
            if number == len(p) - 1:  # 如果只有一个*，那么*号的数量应该是刚好补足了两个字符串的差值。
                return self.dfs(s, "".join(['?' for _ in range(len(s) - number)]) + p[1:])
            else:  # 对应于存在多个*的情况，将*从0到最大长度整体循环一遍就可以得到
                for i in range(len(s) + 1 - number):
                    if self.dfs(s, "".join(['?' for _ in range(i)]) + p[1:]) == True:
                        return True
                return False

        elif s == '' and p != '' or s != "" and p == '':  # 迭代的判别条件:不匹配
            return False


solution = Solution()
print(solution.isMatch(
    "abbabaaabbabbaababbabbbbbabbbabbbabaaaaababababbbabababaabbababaabbbbbbaaaabababbbaabbbbaabbbbababababbaabbaababaabbbababababbbbaaabbbbbabaaaabbababbbbaababaabbababbbbbababbbabaaaaaaaabbbbbaabaaababaaaabb",
    "**aa*****ba*a*bb**aa*ab****a*aaaaaa***a*aaaa**bbabb*b*b**aaaaaaaaa*a********ba*bbb***a*ba*bb*bb**a*b*bb"))
