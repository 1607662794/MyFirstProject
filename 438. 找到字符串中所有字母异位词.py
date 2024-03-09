class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # 方法一：使用内置排序
        if len(s) < len(p):
            return []
        p = "".join(sorted(p))
        result = []
        for i in range(len(s) - len(p) + 1):
            if s[i] not in p:
                continue
            elif "".join(sorted(s[i:i + len(p)])) == p:
                result.append(i)
        return result



solution = Solution()
print(solution.findAnagrams("cbaebabacd", "abc"))
