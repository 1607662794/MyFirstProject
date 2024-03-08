class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = {}
        for i in strs:
            if ''.join(sorted(i)) in result:
                result[''.join(sorted(i))].append(i)
            else:
                result[''.join(sorted(i))] = []
                result[''.join(sorted(i))].append(i)
        return list(result.values())
solution = Solution()
print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))