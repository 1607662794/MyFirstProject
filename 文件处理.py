class Solution(object):
    def minimumDeletions(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        # 这道题的求解思路是，让Word中的每个元素出现的频率不要相差k个
        number = {}
        for i in word:
            if i not in number:
                number[i] = 1
            else:
                number[i] += 1
        number = sorted(number.values())
        # 接下来计算最小的操作数，我用贪心的思想
        global make_number
        make_number = 0

        def greedy(object):
            global make_number
            if len(number) <= 1 or number[-1] - number[0] <= k:
                return
            elif (number[1] - number[0]) * number[0] < (number[-1] - number[-2]) * number[-1]:
                make_number += number[0]
                greedy(object.pop(0))
            else:
                make_number += number[-1]
                greedy(object.pop(-1))

        greedy(number)
        return make_number

solution = Solution()
print(solution.minimumDeletions(word = "aabcaba", k = 0))
