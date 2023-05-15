"""给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。"""
'''算法的时间复杂度应该为 O(log (m+n))'''
'''还有一种解法不需要合并数组，直接找寻对应数值的，空间复杂度更低'''

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        '''合并数组'''
        merge = []
        while nums1 != [] or nums2 != []:
            if nums1 == []:
                merge.append(nums2[0])
                nums2.pop(0)
            elif nums2 == []:
                merge.append(nums1[0])
                nums1.pop(0)
            else:
                if nums1[0] < nums2[0]:
                    merge.append(nums1[0])
                    nums1.pop(0)
                else:
                    merge.append(nums2[0])
                    nums2.pop(0)

        '''二分法求数组中位数'''
        if len(merge) % 2:
            return merge[len(merge) // 2]
        else:
            return (merge[len(merge) // 2 - 1] + merge[len(merge) // 2]) / 2


a = Solution()

print(a.findMedianSortedArrays([1, 2], [3, 4]))



