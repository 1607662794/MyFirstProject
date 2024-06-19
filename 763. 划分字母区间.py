import collections


class Solution(object):  # 合并区间
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        index = collections.defaultdict(int)
        for i, j in enumerate(s):
            index[j] = i  # 记录当前字符最后一次出现的位置。
        result = []
        start = end = 0
        for i, j in enumerate(s):
            end = max(end, index[j])  # 始终记录着当前区间内的最大值
            if end == i:
                result.append(end - start + 1)
                start = i + 1
        return result


s = "ababcbacadefegdehijhklij"
solution = Solution()
print(solution.partitionLabels(s))
