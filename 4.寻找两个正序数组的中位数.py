"""给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。"""
'''算法的时间复杂度应该为 O(log (m+n))'''


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        '''得到两个数组的中位数'''
        return (self.median(nums1) + self.median(nums2)) / 2
        '''合并数组'''
    def median(self, num):

        '''如果该数组长度是奇数，则该数组中位数为最中间的那个数'''
        '''如果该数组长度是偶数，则该数组中位数为最中间两个数的均值'''
        if num==[]:
            return 0
        median_no = len(num) % 2
        if median_no:
            return num[median_no // 2]
        else:
            return (num[median_no // 2 - 1] + num[median_no // 2]) / 2


nums1 = [1, 2]
nums2 = [3, 4]
a = Solution()
print(a.findMedianSortedArrays(nums1, nums2))
