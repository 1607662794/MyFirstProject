class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        three_tuple = []
        '''思路1：如果按照逻辑顺序的话，就是i,j,z定点开始往后移动，但这样时间复杂度将是n^3，难以令人接受'''
        '''思路2：按照值进行求解，先对列表进行排序，先定一个点，然后，另外两个值按照需求进行寻找,时间复杂度n^2'''
        nums.sort()
        for i in range(len(nums) - 2):  # 先定一个点
            j = i + 1
            z = len(nums) - 1
            while j < z:
                if nums[i] + nums[j] + nums[z] < 0:  # 因为小于零，所以需要往大了找
                    j = j + 1
                elif nums[i] + nums[j] + nums[z] > 0:  # 因为大于零，所以需要往小了找
                    z = z - 1
                else:
                    if [nums[i], nums[j], nums[z]] not in three_tuple:
                        three_tuple.append([nums[i], nums[j], nums[z]])
                        j = j + 1  # 因为等于零，所以需要往小和往大了找
                        z = z - 1
        return three_tuple


a = Solution()
print(a.threeSum([-1, 0, 1, 2, -1, -4]))
