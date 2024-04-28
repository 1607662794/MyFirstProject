class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 因数的定义
        if n == 0:
            return False
        while True:
            if n % 5 == 0:
                n = n / 5
            elif n % 3 == 0:
                n = n / 3
            elif n % 2 == 0:
                n = n / 2
            elif n == 1:
                return True
            else:
                return False