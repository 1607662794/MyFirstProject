'''其实你会发现这个字符串的输出是有规律的，你画个Z字形字符串，然后观察输出在字符串中对应的序号，就会发现极其简单'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1: flag = -flag
            i += flag
        return "".join(res)
