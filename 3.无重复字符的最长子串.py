class Solution(object):
    '''给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。'''

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        partion_s = []
        length = 0
        #初始化，同时考虑字符串为空的情况
        while s:
            first_str = s[0]
            s = s[1: ]

            if first_str not in partion_s:
                partion_s.append(first_str)
                length = max(length, len(partion_s))
            # 问题：不止要判断新来的字符串在不在partion_s中，还要判断它在partion_s中的哪一位，需要保留后边的部分
            else:
                partion_s = [first_str]

        return length



