class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #从左到右枚举，找到第i个值前最小的值，然后与当前价格做对比。

        min_index = 0
        max_value = 0
        for i in range(1, len(prices)):
            max_value = max(max_value,prices[i] - prices[min_index])
            if prices[i] < prices[min_index]:
                min_index = i
        return max_value

solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4]))