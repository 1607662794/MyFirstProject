class Solution(object):
    '''我的时间复杂度又是m*n了，我丢，得想个办法，把时间复杂度给降下来'''
    '''我的逻辑方式是，两个循环，一个索引负责字符的索引，另外一个负责数组中元素的索引'''
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        longstrs = ['']
        i = 0
        iter = len(strs)
        while i < len(strs[0]):
            longstr = strs[0][i]
            for j in range(iter):
                if i >= len(strs[j]):
                    return ''.join(longstrs)  # 字符串的连接方式
                else:
                    if strs[j][i] != longstr:
                        return ''.join(longstrs)  # return: 从当前的方法中退出,返回到该调用的方法的语句处,继续执行。
            longstrs.append(longstr)
            i += 1
        longstrs = ''.join(longstrs)  # 貌似没有字符串的连接方式，所以自己做成了字符串列表用来连接
        return longstrs
strs = ["flower", "flow", "flight"]
longestcommonprefix = Solution()
print(longestcommonprefix.longestCommonPrefix(strs))
# a = ['1','b','bc']
# print(max(a))#当列表中的元素都是元组的时候，则会按照元素里面元组的第一个元素的排列顺序，输出最大值，