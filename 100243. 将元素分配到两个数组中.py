class Solution(object):
    def resultArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0 or len(nums) == 1 or len(nums) == 2:
            return nums
        else:
            arr1 = [nums[0]]
            arr2 = [nums[1]]
            for i in range(len(nums)-2):
                if arr1[-1] > arr2[-1]:
                    arr1.append(nums[i + 2])
                else:
                    arr2.append(nums[i + 2])
            return arr1 + arr2

solution = Solution()
print(solution.resultArray([5,4,3,8]))