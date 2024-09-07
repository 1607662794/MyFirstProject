class MinStack(object):

    def __init__(self):
        # 这道题唯一需要注意的是在常数空间内找到最小值，因为每一次连续添加或者删除的数量不定
        # 因此，此处额外构建一个列表来存储当前每个元素对应下的最小值,空间换时间罢了。
        self.stack = []
        self.corr_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if self.corr_stack and self.corr_stack[-1] < val:
            self.corr_stack.append(self.corr_stack[-1])
        elif self.corr_stack and self.corr_stack[-1] >= val:
            self.corr_stack.append(val)
        else:
            self.corr_stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.corr_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.corr_stack[-1]

