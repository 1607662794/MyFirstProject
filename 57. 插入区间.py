# 还有一种更简便的思路，找到与新区间重叠的部分，直接进行合并或者插入即可
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0:
            return [newInterval]

        # 首先进行列表的排序
        inserted_number = len(intervals)  # 如果一直没小于的话，那么就插入到列表的最后一个地方，注意不是lenght-1，而是length。
        for i in range(len(intervals)):
            if newInterval[0] >= intervals[i][0]:
                continue
            inserted_number = i
            break
        intervals.insert(inserted_number, newInterval)

        result = [intervals[0]]
        # 然后对列表进行合并
        for i in range(1, len(intervals)):
            if result[-1][1] > intervals[i][1]:  # 后一个区间在上一个区间之内
                continue
            elif result[-1][1] <= intervals[i][1] and result[-1][1] >= intervals[i][0]:
                result[-1][1] = intervals[i][1]
            else:
                result.append(intervals[i])
        return result


solution = Solution()
print(solution.insert([[1, 5]], [2, 3]))
