# 我的思路是双指针，分别对应相邻的两个“/”，对于如果末尾不以“/”结束的字符串，主动添加一个，然后进行处理即可。
# Leecode的做法是通过split函数分割字符串，然后用列表构建一个栈，从而进行操作！

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        result = ""
        path = path + "/"
        for i in range(len(path) - 1):  # 保证它是第一个“/”索引
            if path[i] == "/":
                for j in range(i + 1, len(path)):  # 保证它是第二个“/”索引
                    if path[j] == "/":
                        if i == j - 1 or path[i + 1:j] == ".":  # 此时两个“/”相连或者表示当前目录
                            break
                        elif path[i + 1:j] == "..":
                            if result != "":
                                length = -1
                                while result[length] != "/":
                                    length -= 1
                                result = result[:length]
                        else:
                            result = result + path[i:j]
                        break
        if result == "":  # 如果最后的目录结局是全部被删光了，那么必须添加一个用于保证正确的输出
            result = "/"
        return result


solution = Solution()
print(solution.simplifyPath("/mYedp/lui/./IS/dpDJF/../A/..///..///..//"))
