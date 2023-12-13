# 我第一次选择的是暴力减法运算，结果果不其然，超时了
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        result = 0
        change = False
        if dividend == -2147483648 and divisor == -1:  # 在该种情况下，运算触及了边界条件，需要进行修正
            return 2147483647
        elif dividend == -2147483648 and divisor == 1 or dividend == 2147483648 and divisor == -1:  # 接下来是两种边界条件，我怕时间超限，所以提前进行框定
            return -2147483648
        elif dividend == 2147483647 and divisor == 1 or dividend == -2147483647 and divisor == -1:
            return 2147483647
        elif dividend < 0 and divisor > 0:
            dividend = -dividend
            change = True
        elif dividend > 0 and divisor < 0:
            divisor = -divisor
            change = True
        elif dividend < 0 and divisor < 0:
            dividend = -dividend
            divisor = -divisor
        # while dividend - divisor >= 0:
        #     dividend = dividend - divisor
        #     result += 1
        remain = dividend  # 余数
        result = 0  # 商
        while remain >= divisor:#力扣上的这个是真的巧妙，每次都基本上用接近一半的数字去减，效率提高地好快
            cur = 1  # 倍增商
            div = divisor  # 倍增值
            while div + div < remain:
                cur += cur
                div += div
            remain -= div  # 余数递减
            result += cur  # 商值累计
        if change:
            return -result
        else:
            return result



solution = Solution()
solution.divide(-2147483648, -2)
