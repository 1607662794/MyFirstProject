'''但我觉得我的这种写法并不是很取巧，肯定还有更好的写法'''
'''另外一种方法是不需要中间再利用列表作为中介，直接数字换数字'''
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        '''考虑特殊情况'''
        a = []
        tag = False
        if x < 0:
            tag = True
            x = -x
        elif x == 0:
            return x

        '''先对其进行数字翻转提取'''
        while x > 0:
            a.append(x % 10)
            x = x // 10

        '''翻转数字'''
        while a != []:
            x = x * 10 + a.pop(0)
        if tag:
            x = x * (-1)
        '''考虑特殊情况'''
        if abs(x) > 2**31:
            return 0

        return x


b = Solution()
print(b.reverse(123))
print(b.reverse(-123))
print(b.reverse(120))
print(b.reverse(1534236469))
print(2**31>1534236469)


