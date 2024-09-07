class Solution(object):
    # '''其实有一种更好的思路是使用递归，而不是我现在的分而求之'''
    # def __init__(self):
    #     self.numnum = ['2', '3', '4', '5', '6', '7', '8', '9']
    #     self.letter = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz', ]
    #     '''初始化一个空列表，然后，不断地往里填充对应字符'''
    #     self.possible = ['']
    #
    # def letterCombinations(self, digits):  # 负责主要工作，不断地将新的字符给加进去
    #     """
    #     :type digits: str
    #     :rtype: List[str]
    #     """
    #     if digits == "":
    #         return []
    #     for i in digits:
    #         self.possible = self.possible * len(self.letter[int(i) - 2])
    #         self.possible.sort()
    #         self.mix(self.possible, self.letter[int(i) - 2])
    #
    #     return self.possible
    #
    # def mix(self, first, second):  # 负责将新的字符串中的字符加入列表，first是一个列表，second是一个字符串
    #     for i in range(len(first)):
    #         self.possible[i] = self.possible[i] + second[i % len(second)]
    def letterCombinations(self, digits):
        hash_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        result = []
        if not digits:
            return result
        result = hash_map[digits[0]]
        digits = digits[1:]
        for i in digits:
            pre_result = result
            result = []
            for j in hash_map[i]:
                result.extend([obj + j for obj in pre_result])
        return result

a = Solution()
print(a.letterCombinations("23"))
