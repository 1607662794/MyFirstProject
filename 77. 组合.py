# 我的思路是使用回溯，从前往后找，终止条件为找到足够数量的组合
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        semi_arrays = []

        def backtrace(start_index):
            if len(semi_arrays) != k:
                for _ in range(start_index, n+1):
                    semi_arrays.append(_)
                    backtrace(_ + 1)
                    semi_arrays.pop()
            else:
                result.append(semi_arrays[:])#不切片的话，存进去的会是一个变量，而非数值
                return

        backtrace(1)
        return result

        # 注释掉的这部分是组合计数的公式计算
        # molecule = 1
        # for _ in range(n):
        #     molecule *= (_ + 1)
        # denominator = 1
        # for _ in range(n-k):
        #     denominator *= (_ + 1)
        # for _ in range(k):
        #     denominator *= (_ + 1)
        # return molecule / denominator


solution = Solution()
print(solution.combine(3, 2))
