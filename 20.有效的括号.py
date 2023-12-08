class Solution(object):
    # 我的思路是，用一个循环，从前往后依次进行一个检查，用消消乐的方式进行消除，如果没有消除则进行保存，有配对成功的则进行消除，思想是和官网统一的，采用栈的形式
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if s == '':
            return True
        elif len(s) % 2 == 1:
            return False
        else:
            fore = [s[0]]
            index = 1
            while index != len(s):
                if len(fore) != 0 and (
                        (fore[-1] == '(' and s[index] == ")") or (fore[-1] == '{' and s[index] == "}") or (
                        fore[-1] == '[' and s[index] == "]")):
                    fore.pop(-1)
                else:
                    fore.append(s[index])
                index += 1
            if fore == []:
                return True
            else:
                return False


solution = Solution()
print(solution.isValid("({[)"))
