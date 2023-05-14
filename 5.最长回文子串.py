'''采用滑动窗口思想进行求解'''
'''这是从里往外找的一种方式'''
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.s = s
        self.head = 0
        self.tail = 0
        self.length = 0
        # 考虑特殊情况，在这种情况下，字符串没有头和尾指标
        if len(s) == 1 or len(s) == 0:
            return s
        else:
            # 对于从内向外的回文字符串判断，有两种情况，一种是两个相同字符串相连，另外一种是中间插了一个字符，然后对称相同，所以做了两次循环
            for i in range(len(self.s) - 1):
                j = i + 1
                # 从内到外判断的初始条件，只有当他们相等的时候才能继续进行下一步
                while i >= 0 and j < len(self.s) and self.s[i] == self.s[j]:
                    # 记录最长回文子串
                    if self.length < len(self.s[i:j + 1]):
                        self.length = len(self.s[i:j + 1])
                        self.head = i
                        self.tail = j
                    i -= 1
                    j += 1
                    # 判断索引是不是还在字符串范围内


            for i in range(len(self.s) - 2):
                j = i + 2
                while i >= 0 and j < len(self.s) and self.s[i] == self.s[j]:
                    if self.length < len(self.s[i:j + 1]):
                        self.length = len(self.s[i:j + 1])
                        self.head = i
                        self.tail = j
                    i -= 1
                    j += 1

            return self.s[self.head:self.tail + 1]


a = Solution()
print(a.longestPalindrome("bb"))
