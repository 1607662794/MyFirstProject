# 刚开始我采用题目分解法，分成两个部分，发现有点问题，更改策略
class Solution(object):
    def __init__(self):
        self.combination = []
        self.conbination_number = []

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        调用下边两个函数，其中一个实现所有字符串的组合，另外一个实现该字符串在s开始索引,但是该方法内存超限，艹
        """
        length = len(words) * len(words[0])
        self.permutations(words, 0, len(words), s, length)
        return list(set(self.conbination_number))

    def permutations(self, arr, position, end, s, length):
        '''使用递归的方法组合所有的字符串'''
        if position == end:
            self.strStr(s, ''.join(arr), length)
        else:
            for index in range(position, end):
                arr[index], arr[position] = arr[position], arr[index]
                self.permutations(arr, position + 1, end, s, length)
                arr[index], arr[position] = arr[position], arr[index]  # 还原到交换前的状态，为了进行下一次交换

    def strStr(self, haystack, needle, length):  # 这个和之前的代码不一样的地方在于，之前的子串长度并不确定，而这道题的子串长度是确定的
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        child = needle[0]
        len_haystack = len(haystack)
        len_needle = len(needle)
        for i in range(len_haystack):
            if (len_haystack - i) < len_needle:
                break
            if haystack[i] != child or haystack[i:i + length] != needle:
                continue
            else:
                self.conbination_number.append(i)


solution = Solution()
s = "barfoothefoobarman"
words = ["foo", "bar"]
print(solution.findSubstring(s, words))
