#看了力扣之后，我有了一个新的思路，就是如果可以消除掉括号的话，就将序号添加至列表里面，如果不可以的话，就将序号剔除出去，最后统计连续数字最长的一段儿。
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        res = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)#对应最左端被放置了)的情况，每次的左指标都是要用于被计算的一个索引
                else:
                    res = max(res, i - stack[-1])#每次都是目前统计最大的连续数和当前的数值相对比
        return res




solution = Solution()
print(solution.longestValidParentheses("))()"))
