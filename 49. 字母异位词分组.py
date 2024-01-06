# 使用哈希表的思路，哈希表的关键字采用每个字符串进行排序后的字符串，字母异位词进行排序后的字符串是一致的。
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash = {}
        for i in strs:
            if ''.join(sorted(i)) not in hash:
                hash[''.join(sorted(i))] = []
                hash[''.join(sorted(i))].append(i)
            else:
                hash[''.join(sorted(i))].append(i)
        result = []
        for i in hash.values():
            result.append(i)
        return result

solution = Solution()
print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
