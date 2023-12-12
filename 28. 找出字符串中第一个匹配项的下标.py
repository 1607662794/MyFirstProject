#有两种情况需要返回-1，一是在haystack中搜索不到needle开头的字母，二是在haystack不包含needle这个子项，我用的方法就是所谓的朴素解法。还有一种比较智慧的方法叫做KMP算法。
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        init = []
        child = needle[0]

        len_haystack = len(haystack)
        len_needle = len(needle)
        for _ in range(len_haystack):#将开头相同的几个序号先给提取出来，然后分别进行检验
            if haystack[_] == child:
                init.append(_)

        #如果找到匹配项目的话，停止后续的查找，并且返回index
        for i in init:
            flag = False
            if (len_haystack-i) < len_needle:#首先判断字符长度够不够，够了的话，那就只需要判断字符串是不是相等
                break
            for j in range(len_needle):
                if haystack[i+j] != needle[j]:
                    flag = True#因为这儿存在最后一个字符不等的情况，所以break没有了效果，考虑到后边还需要进行循环，因此return也不能用
            if flag == False:
                return i
        return -1

solution = Solution()
haystack = "mississippi"
needle = "issip"
print(solution.strStr(haystack, needle))