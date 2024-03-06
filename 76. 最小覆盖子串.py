# 我的思路是定义一个搜索函数，该函数的作用在于搜索t中的字符串是否在s[i,j+1]中，但是事实证明，所有的hard题目中，暴力解法总是会超时。
# leecode中的代码像毛毛虫一样，不断向前蠕动，先包上，然后再缩小。

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        stack = [s if len(s) > len(t) else t]  # need={A:0,B:0,C:0,D:-1,0:-1,E:-1}，needCnt=0

        def search(s, t):  # 我的函数相当于每一次都在重新寻找，而LeeCode相当于在这儿也做了优化，通过构建了一个字典和计数器的方式来进行优化。
            while t != "":
                if t[0] in s:
                    s = s.replace(t[0], '', 1)
                    t = t[1:]
                else:
                    return False
            return True

        if len(s) < len(t):
            return ''

        for i in range(len(s)):
            if s[i] in t and i + len(t) - 1 <= len(s) - 1:  # 第一个字母必须是在t中，是最短子串存在的特征;s子串中还能拥有搜到t长度的空间；
                for j in range(i + len(t) - 1, len(s)):
                    if len(s[i:j + 1]) > len(stack[-1]) or len(stack) != 1 and len(s[i:j + 1]) == len(stack[0]):  # 运用单调栈的思路，只有小于当前栈顶元素的长度才需要进一步检查。
                        break
                    elif s[i:j + 1] == t:
                        return t
                    elif search(s[i:j + 1], t):
                        if len(s[i:j + 1]) == len(t):  # 这种情况证明已经直接找到了t，即最短的子串，因此直接输出即可，不然的话，再慢慢找
                            return s[i:j + 1]
                        stack.append(s[i:j + 1])
                        break  # 如果当前i子串已经找到了的话，在扩大子串就已经没有了意义
        if len(stack) == 1:
            return ""
        else:
            return stack[-1]


solution = Solution()
print(solution.minWindow("A", "ABC"))
