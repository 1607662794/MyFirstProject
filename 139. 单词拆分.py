class Solution(object):
    def wordBreak(self, s, wordDict):
        #背包问题
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if s == "" and '' in wordDict:
            return False
        # def wordbreak(s, wordDict):  # 我的这种方法果然，超时了，因为完全没有剪枝，是一个完全的回溯解法。
        #     if s == "":
        #         return True
        #     else:
        #         result = []
        #         for i in wordDict:
        #             if len(i) <= len(s) and s[:len(i)] == i:
        #                 result.append(wordbreak(s[len(i):], wordDict))
        #         if result == []:
        #             return False
        #         elif any(result):
        #             return True
        #         else:
        #             return False
        #
        # return wordbreak(s, wordDict)
        result = [False for i in range(len(s) + 1)]
        result[0] = True
        for i in range(1, len(s) + 1):
            for j in wordDict:
                if len(j) <= i and s[i-len(j):i] == j:
                    if result[i - len(j)]:  # 用来剪枝，因为只是在寻找可行性，如果找到的话，直接退出即可。
                        result[i] = True
                        break

        return result[-1]


solution = Solution()
print(solution.wordBreak("catsandog",["cats","dog","sand","and","cat"]))
