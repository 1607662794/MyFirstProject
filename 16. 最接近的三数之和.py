class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        '''在上一题目的基础上改，道理是一样的'''
        '''思路1：如果按照逻辑顺序的话，就是i,j,z定点开始往后移动，但这样时间复杂度将是n^3，难以令人接受'''
        '''思路2：按照值进行求解，先对列表进行排序，先定一个点，然后，另外两个值按照需求进行寻找,时间复杂度n^2'''
        nums.sort()
        num = nums[0] + nums[1] + nums[2]
        if nums[-3] + nums[-2] + nums[-1] < target:  # 目标值比最大的三个数相加还大
            return nums[-3] + nums[-2] + nums[-1]
        elif nums[0] + nums[1] + nums[2] > target:  # 目标值比最小的三个数相加还小
            return nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):  # 先定一个点，目标值在列表相加范围以内
            j = i + 1
            z = len(nums) - 1
            while j < z:
                if target - nums[i] - nums[j] - nums[z] < 0:  # 因为三个数的和太大，所以需要往小了找
                    if abs(target - num) > abs(target - nums[i] - nums[j] - nums[z]):
                        num = nums[i] + nums[j] + nums[z]
                    z = z - 1
                elif target - nums[i] - nums[j] - nums[z] > 0:  # 因为三个数的和太小，所以需要往大了找
                    if abs(target - num) > abs(target - nums[i] - nums[j] - nums[z]):
                        num = nums[i] + nums[j] + nums[z]
                    j = j + 1
                else:
                    return target
        return num


a = Solution()
print(a.threeSumClosest([4,0,5,-5,3,3,0,-4,-5], -2))
