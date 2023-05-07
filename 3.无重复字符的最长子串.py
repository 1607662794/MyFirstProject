class Solution(object):
    '''给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。'''

    "重点是滑动窗口概念的运用"
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        partion_s = ''
        length = 0
        # 初始化，同时考虑字符串为空的情况
        while s:
            first_str = s[0]
            s = s[1:]

            if first_str not in partion_s:
                partion_s += first_str
                length = max(length, len(partion_s))

            else:
                #当然也可以用一个指标来进行切片，这样损失一点儿空间，但是极大地提高了时间效率
                # 这种情况下，最大最字符串长度肯定是减的，所以不需要寻找其中的最大值
                partion_s = partion_s.split(first_str)[-1]+first_str

        return length

a = Solution()
a.lengthOfLongestSubstring('aab')
print('abc'.split('b'))