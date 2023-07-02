class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        '''思路：和第15题思路一样，按照值进行求解，先对列表进行排序，先定两个点，第一个点和最后一个点，然后，另外两个值按照需求进行寻找,时间复杂度n^3'''
        four_tuple = []  # 用于存放最后输出的列表列表
        nums.sort()  # 进行排序后才能更方便的进行操作

        if len(nums) < 4:  # 排除特殊情况
            return []
        elif nums[0] + nums[1] + nums[2] + nums[3] > target:  # 这种情况，神仙来了也救不了
            return []
        elif nums[-4] + nums[-3] + nums[-2] + nums[-1] < target:  # 这种情况，神仙来了也救不了
            return []
        else:
            for i in range(len(nums) - 3):  # 因为要使用控制变量法，里面的两个指针已经在不断地变动了，外边的两个就需要控制住
                for j in range(len(nums) - 1, i + 2, -1):
                    z = i + 1
                    k = j - 1
                    while z < k:
                        if nums[i] + nums[j] + nums[z] + nums[k] < target:  # 因为小于零，所以需要往大了找
                            z = z + 1
                        elif nums[i] + nums[j] + nums[z] + nums[k] > target:  # 因为大于零，所以需要往小了找
                            k = k - 1
                        else:
                            if [nums[i], nums[z], nums[k], nums[j]] not in four_tuple:
                                four_tuple.append([nums[i], nums[z], nums[k], nums[j]])
                            z = z + 1  # 因为等于零，所以需要往小和往大了找
                            k = k - 1
            return four_tuple


a = Solution()
print(a.fourSum([2, 2, 2, 2, 2], 8))
