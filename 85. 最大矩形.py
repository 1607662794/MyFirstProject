# 这道题相当于将84题一维的问题扩展到了二维。但因为二维列表的切片与遍历比较麻烦，因此此时不能用暴力求解，不然会很麻烦。
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        # 记录当前位置上方连续“1”的个数
        pre = [0] * (n + 1)
        res = 0
        for i in range(m):
            for j in range(n):
                # 前缀和
                pre[j] = pre[j] + 1 if matrix[i][j] == "1" else 0

            # 单调栈
            stack = [-1]
            for k, num in enumerate(pre):
                while stack and pre[stack[-1]] > num:
                    index = stack.pop()
                    res = max(res, pre[index] * (k - stack[-1] - 1))
                stack.append(k)

        return res
