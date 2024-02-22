# 我的思路是每次看nums2的表头元素应该插入到nums1的哪个位置，每插入一个的同时，将nums1中的最后一个元素弹出。
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i in range(n):#因为nums1的元素是原地修改，所以必须完全替换。
                nums1[i] = nums2[i]
            return nums1
        else:
            j = 0
            for i in range(m+n):
                if j < n and nums2[j] <= nums1[i] or i >= m + j:#因为0不仅可能是在末尾出现，还有可能在中间出现，所以不能用元素等于0来作为条件。
                    nums1.insert(i,nums2[j])
                    nums1.pop(-1)
                    j = j+1
            return nums1

solution = Solution()
print(solution.merge([2,0],1,[1],1))
