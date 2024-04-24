class Solution(object):
    # 遍历整个股票交易日价格列表 price，并执行贪心策略：所有上涨交易日都买卖（赚到所有利润），所有下降交易日都不买卖（永不亏钱）。
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        earn_money = 0
        for i in range(0,len(prices)-1):
            if prices[i] < prices[i+1]:
                earn_money += prices[i+1] - prices[i]
        return earn_money