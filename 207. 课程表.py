from collections import deque


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        indegrees = [0 for i in range(numCourses)]  # 入度表
        adjacency = [[] for i in range(numCourses)]  # 邻接表，用二维矩阵来进行存储

        # 初始化
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)  # 注意这儿是反的比较方便后续的操作。

        # 定义队列，进行进度为0的存储
        queue = deque()

        # 装载进度为0的队列
        for cur in range(len(indegrees)):
            if indegrees[cur] == 0:
                queue.append(cur)

        # 进入循环，将队列循环一遍，如果最后的刚好循环的次数为numCourses的长度，那么则表明结构为有向无环图
        while queue:
            pre = queue.popleft()
            numCourses -= 1
            for cur in adjacency[pre]:
                indegrees[cur] -= 1
                if indegrees[cur] == 0:
                    queue.append(cur)  # 每次执行的都是进度为0的节点
        return not numCourses



