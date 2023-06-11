class Solution(object):
    '''仅适用于纯数字型,将数字转化为列表进行处理'''
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        x = str(x)
        x = [int(x) for x in str(x)]
        fag = True
        while len(x) > 0 :#
            if x[0] != x[-1]:
                fag = False
            if len(x) == 1:
                break
            x.pop(0)
            x.pop(-1)#最后的数字要么是两位要么是一位
        return fag
    '''从数字角度入手，直接将数字颠倒'''
    '''或者直接从字符串出发，顺序表示与倒序表示，每次对比一个'''