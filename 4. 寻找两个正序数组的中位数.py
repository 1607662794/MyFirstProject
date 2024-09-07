class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num = 0
        index = (len(nums1) + len(nums2)) // 2
        if (len(nums1) + len(nums2)) % 2 == 0:
            # 如果是这样的话，则需要返回中间两个数的平均值。
            while nums1 or nums2:
                if nums1 and nums2:
                    if nums1[0] < nums2[0]:
                        current = nums1.pop(0)
                    else:
                        current = nums2.pop(0)
                elif nums2:
                    current = nums2.pop(0)
                else:
                    current = nums1.pop(0)
                if num == index - 1:
                    num1 = current
                elif num == index:
                    num2 = current
                    break
                num += 1
            return (num1 + num2) / 2
        else:
            # 如果不能被整除，只需要找到最中间的一个数即可。
            while nums1 or nums2:
                if nums1 and nums2:
                    if nums1[0] < nums2[0]:
                        current = nums1.pop(0)
                    else:
                        current = nums2.pop(0)
                elif nums2:
                    current = nums2.pop(0)
                else:
                    current = nums1.pop(0)
                if num == index:
                    break
                num += 1
            return current



solution = Solution()
print(solution.findMedianSortedArrays([1,2],[3,4]))