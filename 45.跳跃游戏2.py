# 对于这道题，我的思路是采用BFS的方法进行搜索，每次搜索，存储当前找寻次数下抵达的下标索引。
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        target = 0  # 看看当前走了几步
        bfs = [nums[0]]  # 存放当前步数下的列表索引
        while True:
            for i in bfs:
                bfs_1 = []
                for j in range(nums[i]):
                    if i + j + 1 == len(nums):
                        return target
                    elif i + j + 1 > len(nums):
                        continue
                    else:
                        if i + j + 1 not in bfs_1:
                            bfs_1.append(target + j + 1)
            bfs = bfs_1
            target = target + 1


solution = Solution()
print(solution.jump([2,3,0,1,4]))
