class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # s = '1[' + s + ']'
        stack_1 = []  # 用于存放数字
        stack_2 = []  # 用于存在子串
        number = 0
        string = ''
        for i in range(len(s)):
            if s[i] == '[':
                stack_1.append(number)  # 添加当前数字和上一组子串
                stack_2.append(string)
                number = 0
                string = ''
            elif s[i] == ']':
                a = stack_2.pop()
                b = stack_1.pop()
                string = a + b * string
            elif ord(s[i]) <= 57 and ord(s[i]) >= 48:
                number = 10 * number + int(s[i])
            else:
                string += s[i]
        return string



