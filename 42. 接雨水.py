# 我的思路是采用动态规划收集所有的局部最高点，形成凹槽，然后计算每个凹槽里面的容水量，具体做法为根据左右两边的较小值乘以长度，然后减去长度内容的数值。
# 力扣上一行一行往上推导计算的也很奇特，但是时间复杂度没有这个好
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 2:  # 对于只有两个数值的列表，则无法积水
            return 0
        local_rain = []
        local_peak = self.find_local_peak(height)
        if len(local_peak) == 1 or len(local_peak) == 0:  # 对于只有一个极值点或者零个极值点的列表，无法积水
            return 0
        for index, value in enumerate(local_peak):
            if index == 0:
                continue
            else:
                area = (value - local_peak[index - 1] - 1) * min(height[value], height[
                    local_peak[index - 1]])  # 其中包含了对于两个极值点相邻的情况，因为中间没有夹缝，所以不用计算的状况
                for i in range(value - local_peak[index - 1] - 1):
                    if height[value - i - 1]>min(height[value], height[local_peak[index - 1]]):#对于极值点中间超过最小值的部分，则只需要减去最小值即可，不需要完全减去
                        area = area - min(height[value], height[local_peak[index - 1]])
                    else:
                        area = area - height[value - i - 1]
                local_rain.append(area)
        rain = sum(local_rain)
        return rain

    def find_local_peak(self, height):
        # 该函数用于找到数字数组中的局部最大值，然后因为只有呈现波峰形状的数值列表才能计算盛水量，所以需要对第一遍找到的极值点进行进一步处理。
        # step 1:找到局部最大值，并找到所有极值点中的最大值，也就是全局最大值
        if len(height) <= 2:  # 对于只有两个数值的列表，则无法积水
            return 0
        local_peak = []  # local_peak存储极值点在height中的序号
        index = 0
        index_max = 0  # 最大值在local_peak中的序号
        max = height[index_max]
        while index <= len(height) - 1:
            if index == 0:
                if height[index] > height[index + 1]:
                    local_peak.append(index)
            elif index == len(height) - 1:
                if height[index] > height[index - 1]:
                    local_peak.append(index)
                    if height[index] > max:
                        max = height[index]
                        index_max = len(local_peak) - 1  # max每更新一次，index_max相应更新一次
            elif height[index] >= height[index - 1] and height[index + 1] <= height[index]:
                local_peak.append(index)
                if height[index] > max:
                    max = height[index]
                    index_max = len(local_peak) - 1  # max每更新一次，index_max相应更新一次
            index += 1

        # step 2:根据绝对最大值，筛除极大值中的假值
        index = 0
        while index < len(local_peak):
            if index_max >= 2 and index < index_max:  # 在最大值左侧，并且有可能需要删除极值点的情况
                if index > 0 and height[local_peak[index]] < height[local_peak[index - 1]]:
                    local_peak.pop(index)
                    index_max -= 1
                    continue
            elif index_max <= len(local_peak) - 3 and index > index_max:  # 在最大值右侧，并且有可能需要删除极值点的情况
                if height[local_peak[len(local_peak) + index_max - index - 1]] < height[
                    local_peak[len(local_peak) + index_max - index]]:
                    local_peak.pop(len(local_peak) + index_max - index - 1)
                    continue
            index = index + 1
        return local_peak


solution = Solution()
print(solution.trap([1000,999,998,997,996,995,994,993,992,991,990,989,988,987,986,985,984,983,982,981,980,979,978,977,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966,966]))
