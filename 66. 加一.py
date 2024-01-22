# 对于这一道题的思路是：只关注于当前位，考虑进位的话，有两种特殊情况，一是在首尾，需要列表多增加一位，而是在其他位置，需要进位，不考虑进位的话，直接输出即可。
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        add = 1
        for i in range(len(digits) - 1, -1, -1):
            if add == 0:
                return digits
            elif add == 1 and digits[i] == 9 and i == 0:
                digits[i] = 0
                digits.insert(0, 1)
            elif add == 1 and digits[i] == 9 and i != 0:
                digits[i] = 0
            else:
                digits[i] += 1
                add = 0
        return digits

solution = Solution()
print(solution.plusOne([9]))
