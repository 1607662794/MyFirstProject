# 这道题同样是二分搜索，最后的情况会被统一排挤到剩下0个或者1个的状态，对于零个，则为插入，对于一个，如果大了就放在右边，如果小了，就放在左边
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        #     index = self.search(nums, target, 0, len(nums) - 1)
        #     return index
        #
        # def search(self, nums, target, l, r):  # 二分法搜索
        #     if r == -1 or (r - l) == 1 and nums[l] > target:  # 最后的情况要么是两个要么是一个或者刚开始直接输入的空列表
        #         return l
        #     elif (r - l) == 0 and nums[l] < target:
        #         return l + 1
        #     elif (r - l) == 0 and nums[l] > target:
        #         return l
        #     elif nums[(l + r) // 2] < target:
        #         return self.search(nums, target, l=(l + r) // 2 + 1, r=r)
        #     elif nums[(l + r) // 2] > target:
        #         return self.search(nums, target, l=l, r=(l + r) // 2 - 1)
        #     else:
        #         return (l + r) // 2
        def search(l, r):
            if l > r:
                return l+1
            elif target == nums[(l + r) // 2]:
                return (l + r) // 2
            if target > nums[(l + r) // 2]:
                return search((l + r) // 2 + 1, r)
            else:
                return search(l, (l + r) // 2 - 1)

        return search(0, len(nums) - 1)


solution = Solution()
print(solution.searchInsert([1, 3, 5, 6], 1))
