# 我的思路是使用回溯，比如一个**+*+**的列表，其中中间的*号是最小值，那么这个列表中最大的矩形面积，要么是底部一层，要么就是左右两部分矩形。
# Leecode使用的是单调栈的思路，而我的方法总是超时。
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # 方法一：暴力求解
        # area = 0
        # for i in range(len(heights)):
        #     for j in range(i, len(heights)):
        #         if area < min(heights[i:j+1])*(j-i+1):
        #             area = min(heights[i:j+1])*(j-i+1)

        # 方法二：动态规划

        area = {}

        def dp(i, j):
            if (i, j) in area:
                return area[(i, j)]
            elif i == j:
                area[(i, j)] = heights[i]
                return area[(i, j)]
            else:
                if len(set(heights[i:j + 1])) == 1:
                    area[(i, j)] = sum(heights[i:j + 1])
                    return area[(i, j)]
                else:
                    index = i + heights[i:j + 1].index(min(heights[i:j + 1]))
                    if index == i:
                        area[(i, j)] = max(heights[index] * (j - i + 1), dp(index + 1, j))
                        return area[(i, j)]
                    elif index == j:
                        area[(i, j)] = max(heights[index] * (j - i + 1), dp(i, index - 1))
                        return area[(i, j)]
                    else:
                        area[(i, j)] = max(heights[index] * (j - i + 1), dp(i, index - 1), dp(index + 1, j))
                        return area[(i, j)]

        dp(0, len(heights) - 1)
        return max(area.values())

solution = Solution()
print(solution.largestRectangleArea([4,9,3,3,9,9,2,1,8,4,2,3,0,3,0]))
