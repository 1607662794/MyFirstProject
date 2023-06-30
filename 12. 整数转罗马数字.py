class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        rule = {1: 'I', 5: 'V', 10: 'X', 50: "L", 100: 'C', 500: 'D', 1000: 'M'}

        # 分成两部分进行考虑，一部分是1,10,100,1000，另一部分是5,50,500，其实更好的方式是将所有的数字都给列出来，暴力求解
        keys = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        values = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        Roamn = ''

        for i in range(len(keys) - 1, -1, -1):
            res = num // keys[i]
            num %= keys[i]
            Roamn += values[i] * (res)
        return Roamn


a = Solution()
a.intToRoman(1994)