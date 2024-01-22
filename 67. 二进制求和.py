# 我的思路是，从后往前依次相加，算上进位的数字，相加后的结果位于0到3，分别考虑边界条件与内部条件，分别进行模拟即可。
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        add = 0
        a = list(a)
        b = list(b)
        for i in range(-1, -max(len(a), len(b)) - 1, -1):
            # 首先对于两者不齐的情况，通过零来进行补齐
            if len(a) > len(b) and i < -len(b):  # b此时要短一点
                b.insert(0, '0')
            elif len(a) < len(b) and i < -len(a):  # a此时要短一点
                a.insert(0, '0')

            if i == -max(len(a), len(b)) and add + int(a[i]) + int(b[i]) == 3:  # 边界条件
                a[i] = '1'
                a.insert(0, '1')
                return ''.join(a)
            elif i == -max(len(a), len(b)) and add + int(a[i]) + int(b[i]) == 2:  # 边界条件
                a[i] = '0'
                a.insert(0, '1')
                return ''.join(a)
            elif i == -max(len(a), len(b)) and add + int(a[i]) + int(b[i]) == 1:  # 边界条件
                a[i] = '1'
                return ''.join(a)
            elif i == -max(len(a), len(b)) and add + int(a[i]) + int(b[i]) == 0:  # 边界条件
                return ''.join(a)
            elif add + int(a[i]) + int(b[i]) == 3:  # 内部条件
                a[i] = '1'
                add = 1
            elif add + int(a[i]) + int(b[i]) == 2:  # 内部条件
                a[i] = '0'
                add = 1
            elif add + int(a[i]) + int(b[i]) == 1:  # 内部条件
                a[i] = '1'
                add = 0
            else:  # 内部条件
                add = 0


soluition = Solution()
print(soluition.addBinary('11', '1'))
