# 我的思路是定义一个函数，这个函数的功能在于在一个子字符串中寻找一定数量的IP地址的子串，每一次传入函数中的，不只有所需子串数量，还有已经组好的子串，这样就解决了每次需要复制的问题。
# LeeCode中的解法是将字符串划分成了4段，然后进行满足要求的回溯。
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        if len(s) < 4:
            return result
        head = 0
        tail = len(s) - 1

        def backtrace(substring, number, head, tail):
            if head == tail+1 and number == 0:  # 找到了正确的组合的情况
                result.append(substring)
            elif tail - head + 1 < number or number == 0 and head != tail+1:  # 肯定找不出来的情形
                return
            elif s[head] == '0':
                if substring == "":
                    substring = '0'
                else:
                    substring = substring + "." + '0'
                backtrace(substring, number - 1, head + 1, tail)
            else:
                if substring == "":
                    backtrace(s[head], number - 1, head + 1, tail)
                else:
                    backtrace(substring + "." + s[head], number - 1, head + 1, tail)

                if tail - head + 1 >= 2:
                    if substring == "":
                        backtrace(s[head:head + 2], number - 1, head + 2, tail)
                    else:
                        backtrace(substring + "." + s[head:head + 2], number - 1, head + 2, tail)
                if tail - head + 1 >= 3 and int(s[head:head + 3]) <= 255:
                    if substring == "":
                        backtrace(s[head:head + 3], number - 1, head + 3, tail)
                    else:
                        backtrace(substring + "." + s[head:head + 3], number - 1, head + 3, tail)
        backtrace("",4,head,tail)
        return result
solution = Solution()
print(solution.restoreIpAddresses("101023"))