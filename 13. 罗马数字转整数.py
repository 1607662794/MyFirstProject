class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 列出所有规则的字典，让字符串从右往左开始寻找
        keys = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        values = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
#         rule = dict(zip(keys, values))
        num = 0
        i = len(keys)-1
        while i >= 0 and s != '':
            if s[0] == values[i]:#这儿注意索引和切片的区别
                s = s[1:]
                num += keys[i]
            elif s[0:2] == values[i]:
                s = s[2:]
                num += keys[i]
                i -= 2
            else:
                i -= 1
        return num


a = Solution()
a.romanToInt("LVIII")