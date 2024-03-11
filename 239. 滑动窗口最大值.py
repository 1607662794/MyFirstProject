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
        ans = []
        q = deque()  # 双端队列
        for i, x in enumerate(nums):
            # 1. 入
            while q and nums[q[-1]] <= x:  # 保证x值是当前栈中的最小值。
                q.pop()  # 维护 q 的单调性
            q.append(i)  # 入队
            # 2. 出
            if i - q[0] >= k:  # 队首已经离开窗口了
                q.popleft()
            # 3. 记录答案
            if i >= k - 1:
                # 由于队首到队尾单调递减，所以窗口最大值就是队首
                ans.append(nums[q[0]])
        return ans

solution = Solution()
print(solution.maxSlidingWindow(nums = [1,2,3,4,5], k = 3))