# 这算法太牛逼了，使用哈希（字典）的方式进行存储，然后动态规划求解
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        dp = {i: [] for i in range(target + 1)}  # 定义一个空字典，可以当哈希使用，dp是动态规划的简称。

        # 这里一定要将candidates降序排列
        for i in sorted(candidates, reverse=True):  # 倒序查找的原因在于：没有漏的，也没有多于加的。顺序查找的话，会有重复值。有了最大的数可以求什么，有了次大的数可以求什么，不断往下走。
            for j in range(i, target + 1):
                if j == i:  # 如果有了的话，那么先给每个字典或者哈希将本身放进去
                    dp[j] = [[i]]
                else:
                    dp[j].extend([x + [i] for x in dp[j - i]])  # 为不是本身的数，在前面找，如果没有的话，因为没有进入循环，所以没有增添新的数字。
        return dp[target]


solution = Solution()
print(solution.combinationSum([1, 2, 4], 6))
