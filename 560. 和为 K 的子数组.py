# 我的思路是，使用双指针，每次计算这个双指针规定的子串的和，如果超了，则子串缩小，如果不够，则子串扩大，值得注意的是，这种方法仅仅适合有序排列的数组，对于无序排列的数组只能使用暴力求解。
import collections


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 方法一：有序数列下的计算
        # sum = 0  # 用于存储已经计算过的和，减少计算量
        # result = 0
        # j = 0
        # for i in range(len(nums)):
        #     while j < len(nums) and sum + nums[j] < k:
        #         sum += nums[j]
        #         j += 1
        #     if sum + nums[j] == k:
        #         result += 1
        #         sum = k
        #     else:
        #         sum -= nums[i]
        # return result
        # 方法二：暴力求解，会超时
        # result = 0
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         if sum(nums[i:j+1]) == k:
        #             result += 1
        # return result
        # 方法三：动态规划-空间换时间,但这样空间超过限制
        # result_sum = {}
        # result = 0
        # def dp(i, j):
        #     if (i, j) in result_sum:
        #         return result_sum[(i, j)]
        #     elif i == j:
        #         result_sum[(i, j)] = nums[i]
        #         return result_sum[(i, j)]
        #     else:
        #         result_sum[(i, j)] = nums[j] + dp(i, j - 1)
        #         return result_sum[(i, j)]
        #
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         if dp(i, j) == k:
        #             result += 1
        #     # 每循环一圈之后，其实可以将空间清空一次，因为已经用不到了
        #     result_sum = {}
        # return result
        # Leecode使用前缀和的思路来进行求解。pre[i]−pre[j−1]==k →→ pre[j−1]==pre[i]−k
        num_times = collections.defaultdict(int)
        num_times[0] = 1  # 先给定一个初始值，代表前缀和为0的出现了一次
        cur_sum = 0  # 记录到当前位置的前缀和
        res = 0
        for i in range(len(nums)):
            cur_sum += nums[i]  # 计算当前前缀和
            if cur_sum - k in num_times:  # 如果前缀和减去目标值k所得到的值在字典中出现，即当前位置前缀和减去之前某一位的前缀和等于目标值
                res += num_times[cur_sum - k]
            # 下面一句实际上对应两种情况，一种是某cur_sum之前出现过（直接在原来出现的次数上+1即可），
            # 另一种是某cur_sum没出现过（理论上应该设为1，但是因为此处用defaultdict存储，如果cur_sum这个key不存在将返回默认的int，也就是0）
            # 返回0加上1和直接将其置为1是一样的效果。所以这里统一用一句话包含上述两种情况
            num_times[cur_sum] += 1
        return res
solution = Solution()
print(solution.subarraySum([1, 2, 3], 3))
