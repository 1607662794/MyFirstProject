# 对于这道题，我的思路是采用BFS的方法进行搜索，每次搜索，存储当前找寻次数下抵达的下标索引。
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if len(nums) <= 1:
        #     return 0
        # elif nums[0] >= len(nums) - 1:
        #     return 1
        # # 接下来这段代码实现的是广度优先算法，但是在面临极大的计算算例是会出现时间超限的问题。
        # step = 0  # 看看当前走了几步
        # current_index = [0]  # 存放当前步数下的列表索引
        # while True:
        #     step = step + 1
        #     current_index_1 = []
        #     for i in current_index:
        #         for j in range(nums[i], 0, -1):
        #             if i + j == len(nums) - 1:
        #                 return step
        #             elif i + j > len(nums) - 1:
        #                 continue
        #             else:
        #                 if i + j not in current_index_1 and i+j not in current_index:#剪枝操作：对于在当前步数下，存储的索引不必重复搜索，对于当前步数下计算出来的索引之前出现过，也不必重复索引，肯定不是最短路径
        #                     current_index_1.append(i + j)
        #     current_index = current_index_1

        # 因此接下来这段代码实现的是深度优先算法。不能使用深度优先算法，因为它不一定是最短的步数。
        # 看到贪心算法后，想到了一种新的解法，最后的目标值肯定能够到达，所采取的方式即为在当前步下，所能到达的最远值，索引+数值。
        
        # current_index = 0
        # step = 0
        # while True:
        #     max = nums[current_index]
        #     for i in range(1, nums[current_index] + 1):
        #         if current_index + i + nums[current_index + i] >= len(nums)-1:
        #             return step + 2
        #         elif current_index + i + nums[current_index + i] > max:
        #             max = current_index + i + nums[current_index + i]
        #             max_index = current_index + i
        #     current_index = max_index
        #     step += 1

        i = 0
        step = 0
        if len(nums) == 1:
            return 0
        if nums[0] >= len(nums) - 1:
            return 1
        while i < len(nums) - 1:
            far_distance = i + nums[i]
            max_index = i
            for j in range(i, i + nums[i] + 1):
                if j + nums[j] > far_distance:
                    far_distance = j + nums[j]
                    max_index = j
            i = max_index
            step += 1
        return step

solution = Solution()
print(solution.jump([1,2,3]))
