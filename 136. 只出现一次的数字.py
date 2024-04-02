class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = []
        for i in nums:
            if i not in result:
                result.append(i)
            else:
                result.remove(i)
        return result[0]
solution = Solution()
print(solution.singleNumber([2,2,1]))