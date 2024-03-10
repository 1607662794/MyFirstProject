class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        app_number = sum(apple)
        capacity = sorted(capacity, reverse=True)
        for i in range(len(capacity)):
            app_number -= capacity[i]
            if app_number <= 0:
                return i+1
solution = Solution()
print(solution.minimumBoxes(apple = [5,5,5], capacity = [2,4,2,7]))
