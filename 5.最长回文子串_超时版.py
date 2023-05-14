'''采用滑动窗口思想进行求解'''
'''这是从外往里找的一种方式，当然，这种方式的时间复杂度太大，LeeCode甚至都超时了，我刚才想到，如果从里往外找，岂不是更简单，'''


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        '''主函数，只负责指点江山，调用子函数'''
        self.s = s
        self.head = 0
        self.tail = 0
        self.length = 0

        if len(s) == 1 or len(s) == 0:
            return s
        else:
            return self.collect_string()

    def collect_string(self):
        '''子函数用于收集子字符串，两个索引，一旦后一个字符出现，则在前面找这个字符，这两个字符间构成子字符串'''
        for j in range(1, len(self.s)):
            for i in range(j):
                '''嵌套循环，尾巴索引依次向后，头索引不能碰到尾巴索引，并从头开始，依次检查，也只能从头开始依次检查，比如说，从abccb到abccba'''
                if self.s[i] == self.s[j]:
                    '''子字符串是回文子串的必要条件是边界上的两个字符相同，根据这一特点，提取子串，进行处理'''
                    if self.judge_sym(self.s[i:(j+1)]):
                        '''判断这个子串'''
                        if self.length < len(self.s[i:j+1]):
                            self.length = len(self.s[i:j+1])
                            self.head = i
                            self.tail = j

        return self.s[self.head:self.tail+1]

    def judge_sym(self, s):
        '''子函数用于判断这个列表是否是回文字符串'''
        for i in range(len(s) // 2):
            if s[1] != s[-2]:
                return False
            else:
                s = s[1:-1]
        return True
a = Solution()
print(a.longestPalindrome("babad"))