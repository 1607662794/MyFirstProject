# 我的思路是使用回溯方法，依次将所有的元素提前，然后进行操作，操作结束后，再将提前的元素复原。
# 这个就是之前的思路，就是每次固定一位数字，该数字可以有剩余字母中一一填充，从而筛选出所有组合。
# 然而这道题完全可以根据数学来进行推导，因为次序是确定的。
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        allFactorial = [1, 1]
        for i in range(2, n + 1):
            allFactorial.append(allFactorial[-1] * i)  # 阶乘结果存储

        s, k, res = list(range(1, n + 1)), k - 1, ""
        for i in range(len(s) - 1, -1, -1):
            res += str(s[k // allFactorial[i]])
            del s[k // allFactorial[i]]
            k %= allFactorial[i]
        return res

solution = Solution()
print(solution.getPermutation(3,3))