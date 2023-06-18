class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        '''我的思路是，先构造一个数据链表，用于存储我们需要的这种数据'''

        '''通过嵌套两重循环来遍历数据，查询哪种组合的面积最大'''
