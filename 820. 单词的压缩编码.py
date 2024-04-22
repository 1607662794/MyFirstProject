class Solution(object):
    # 这道题其实可以使用字典树进行求解
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        list_words = sorted(words, key=lambda x: len(x), reverse=True)  # 排序字典后即为列表
        i = 0
        while i < len(list_words):
            j = i + 1
            while j < len(list_words):
                if list_words[j] == list_words[i][-len(list_words[j]):]:
                    list_words.pop(j)
                    continue
                else:
                    j = j + 1
            i += 1
        length = 0
        for i in range(len(list_words)):
            length = length + len(list_words[i]) + 1
        return length


solution = Solution()
print(solution.minimumLengthEncoding(["time", "me", "bell"]))
