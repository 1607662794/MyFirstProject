class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if '.' not in p and '*'not in p:
            if s!=p:
                return False
        if p == '.*':
            return True
        if '.' in p and '*' not in p:
            if len(s) == len(p):
                for i in len(s):
                    if p[i]!='.':
                        if p[i]!=s[i]:
                            return False
                return True
            else:
                return False
        if '.' not in p and '*' in p: