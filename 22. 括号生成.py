# 这个题我一时想不到什么，这题可以用动态规划法解答，也可以使用深度优先搜索法，在本题中是同一种方法
class Solution:
    def generateParenthesis(self, n: int):
        if n <= 0: return []
        res = []

        def dfs(paths, left, right):
            if left > n or right > left: return
            if len(paths) == n * 2:  # 因为括号都是成对出现的
                res.append(paths)
                return
            #任何一个分支后边可以加左括号，也可以加有括号
            dfs(paths + '(', left + 1, right)  # 生成一个就加一个
            dfs(paths + ')', left, right + 1)

        dfs('', 0, 0)
        return res


solution = Solution()
print(solution.generateParenthesis(n=3))
