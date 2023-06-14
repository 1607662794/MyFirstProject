class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # 第一种情况，
        if '*' not in p:
            if len(p) != len(s):
                return False
            else:
                for i in range(len(s)):
                    if p[i]!='.':
                        if p[i]!=s[i]:
                            return False
                return True
        else:
            # tag_1 = False
            # tag_2 = False

            for i in p:
                for j in s:
                    '''为了使用滑动窗口，依次对比而设置的一些参数'''
                    if i == '.':
                        tag_1 = True#记录‘.’
                    elif j == '*':
                        tag_2 = True
                    else:
                        tag_1,tag_2 = False,False
                        tag_3 = i
                    if i != '.':
