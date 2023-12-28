# 标准的回溯，从前往后找，如果后边的组合和当前的数能够合成目标值，则输出，如果不能则继续往后找，其中值得注意的地方在于，如果存在重复值，则可能会出现重复组合，在这种情况下，需要进行剪枝continue来进行避免。
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        result = []
        candidates.sort()

        def backtrack(candidates, tmp):
            if sum(tmp) > target: return
            if sum(tmp) == target:
                result.append(tmp)
                return

            for i in range(len(candidates)):
                if i > 0 and candidates[i] == candidates[i - 1]:
                    continue
                backtrack(candidates[i + 1:], tmp + [candidates[i]])
            return result

        return backtrack(candidates, [])


solution = Solution()
print(solution.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
