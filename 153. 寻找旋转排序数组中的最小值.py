class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #遍历查找
        #for i in range(len(nums)-1):
        #    if nums[i] > nums[i+1]:
        #        return nums[i+1]
        #return nums[0]
        #如果非要满足对数时间复杂度查找，那么可以分成两步，第一步找到满足条件的递增序列，第二步在递增序列中寻找最小值
        #如果中间值小于最后一个值，那么最小值一定在左侧。如果中间值大于最后一个值，那么最小值一定在右侧
        #可以想象两个三角形来进行处理。
        i = 0
        j = len(nums)-1
        while i < j:
            mid = (i + j) // 2
            if nums[mid] < nums[j]:
                j = mid
            else:
                i = mid + 1
        return nums[j]