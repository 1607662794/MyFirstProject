class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # s = '1[' + s + ']'
        # stack_1 = []  # 用于存放数字
        # stack_2 = []  # 用于存在子串
        # number = 0
        # string = ''
        # for i in range(len(s)):
        #     if s[i] == '[':
        #         stack_1.append(number)  # 添加当前数字和上一组子串
        #         stack_2.append(string)
        #         number = 0
        #         string = ''
        #     elif s[i] == ']':
        #         a = stack_2.pop()
        #         b = stack_1.pop()
        #         string = a + b * string
        #     elif ord(s[i]) <= 57 and ord(s[i]) >= 48:
        #         number = 10 * number + int(s[i])
        #     else:
        #         string += s[i]
        stack = []
        number = 0
        word = ''
        for i in range(len(s)):
            if '0' <= s[i] <= '9':
                number = number * 10 + int(s[i])
            elif s[i] == '[':
                stack.append([word,number])
                word = ''
                number = 0
            elif s[i] == ']':
                last_word, cur_number = stack.pop()
                word = last_word + cur_number * word
            else:#对应着字母字符
                word += s[i]
        return word

solution = Solution()
print(solution.decodeString("3[a2[c]]"))



