class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        tag = 1
        if s == '':
            return 0
        while s[0] == " ":
            s = s[1:]
            if s == '':
                return 0
        if s[0] == "-":
            tag = -1
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]
        for i in range(len(s)):
            if ord(s[0]) >= 48 and ord(s[0]) <= 57:
                num = num * 10 + ord(s[0]) - 48
            else:
                break
            s = s[1:]
        if (num * tag) < -2 ** 31:
            return -2 ** 31
        elif (num * tag) > ((2 ** 31) - 1):
            return 2 ** 31 - 1
        else:
            return num * tag


a = Solution()
print(a.myAtoi("-"))
