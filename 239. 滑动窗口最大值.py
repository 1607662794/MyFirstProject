import heapq
from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 我的解法是暴力求解，时间会超限
        # if k == 1:
        #     return nums
        # max_value = []
        # for i in range(len(nums) - k + 1):
        #     if i >= 1 and nums[i] > max_value[-1]:
        #         max_value.append(nums[i])
        #         continue
        #     max_value.append(max(nums[i:i+k]))
        # return max_value
#       # LeeCode的解法使用单调栈的思路
#         n = len(nums)
#         # 注意 Python 默认的优先队列是小根堆
#         q = [(-nums[i], i) for i in range(k)]
#         heapq.heapify(q)
#
#         ans = [-q[0][0]]
#         for i in range(k, n):
#             heapq.heappush(q, (-nums[i], i))
#             while q[0][1] <= i - k:
#                 heapq.heappop(q)
#             ans.append(-q[0][0])
#
#         return ans

        n = len(nums)
        # 注意 Python 默认的优先队列是小根堆
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)
        print(q)
        ans = [-q[0][0]]
        print(-q[0][0])
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
                heapq.heappop(q)
            ans.append(-q[0][0])

        return ans
solution = Solution()
print(solution.maxSlidingWindow(nums = [3,2,4,1,5], k = 3))