# 其实还可以更简单，排完序号后的列表直接依次往里面放，对于没有重叠的部分，直接放，有重叠部分的，直接更改前一个值
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) <= 1:
            return intervals
        # 首先进行列表的排序
        intervals = sorted(intervals, key=lambda intervals: intervals[0])

        current_interval = intervals[0]
        result = []

        for i in range(len(intervals)):  # 当遇到一个新的区间之外的区间或者抵达列表末尾的时候进行一次添加
            if i >= 1 and intervals[i] == intervals[i - 1] and i != len(intervals) - 1:  # 前后两个区间完全相同
                continue
            elif i >= 1 and intervals[i] == intervals[i - 1] and i == len(intervals) - 1:
                result.append(current_interval)
            elif intervals[i][0] >= current_interval[0] and intervals[i][1] <= current_interval[1] and i != len(
                    intervals) - 1:  # 后一个区间完全在前一个区间内部。
                continue
            elif intervals[i][0] >= current_interval[0] and intervals[i][1] <= current_interval[1] and i == len(
                    intervals) - 1:  # 后一个区间完全在前一个区间内部。
                result.append(current_interval)
            elif intervals[i][0] <= current_interval[1] and i != len(
                    intervals) - 1:  # 后一个区间插入了前一个区间的部分，此时当前区间仅进行更新就好，但不需要添加进结果里面。
                current_interval[1] = intervals[i][1]
            elif intervals[i][0] <= current_interval[1] and i == len(
                    intervals) - 1:  # 后一个区间插入了前一个区间的部分，此时当前区间进行更新，需要添加进结果里面。
                current_interval[1] = intervals[i][1]
                result.append(current_interval)
            else:  # 其余情况为，后一个区间没有插入前一个区间，此时直接将当前区间插入结果就好，并对当前区间进行更新。
                result.append(current_interval)
                current_interval = intervals[i]
                if i == len(intervals) - 1:  # 同样需要将边界条件封印起来
                    result.append(current_interval)

        return result


solution = Solution()
print(solution.merge([[0, 2], [0, 1], [0, 0], [2, 3], [4, 4], [4, 5], [5, 7]]))
