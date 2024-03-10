# 我的思路是每次都在当前列表中的最大值与0之间选择最大值，并将最后的结果进行保存。
class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        result = 0
        happiness.sort(reverse=True)  # 如果每次都重新寻找最大值的话，会导致超时
        for i in range(k):
            result += max(happiness[0] - i, 0)
            happiness.pop(0)
        return result


solution = Solution()
print(solution.maximumHappinessSum(happiness=[1, 2, 3], k=2))
