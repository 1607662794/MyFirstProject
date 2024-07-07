# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 我的思路仍然是采用前缀和与回溯结合的方法
        # 前缀和用于表示任何一个节点到根节点的距离，之前的题目因为最后求解的是一个定值，因此可以在之前的前缀和中进行寻找
        # 但是现在是要求最大路径和，因此，要是仍然按照那种方式进行寻找的话，绝对会出问题。
        # 因此，我的思路是同时存储一个最大值与最小值，然后随时进行相减以检查是否达到了最大路径和
        # 卧槽，突然发现，前缀和的方式其实并不行，因为这个节点序列，并不是一定需要从根节点开始算起。

        #self.max = 0
        # def backtrace(root, prefix, min_sum):
        #     if not root:
        #         return
        #     prefix.append(prefix[-1] + root.val)
        #     if prefix[-1] < min_sum:
        #         min_sum = prefix[-1]
        #     if prefix[-1] - min_sum > self.max:
        #         self.max = prefix[-1] - min_sum  # 这儿也可以用官方题解，字典的形式。
        #     backtrace(root.left, prefix, min_sum)
        #     backtrace(root.right, prefix, min_sum)
        #     prefix.pop()
        # backtrace(root, [0], 0)  # 第一个零，既是为了列表的完整性，同时也是代表取当前节点等于求和值的情况。
        # return self.max

        # 因此这道题的思路是使用了动态规划，每一个非空节点作为根节点的最大路径之和为该节点本身加其左右节点的最大贡献值，这样的话，就实现了状态转移
        # 边界条件为，边节点上的最大贡献值即为本节点本身，空节点的最大贡献值为0
        self.maxSum = float('-inf')
        def maxGain(node):
            if not node:
                return 0
            leftGain = max(maxGain(node.left),0)#0表示不取该值
            rightGain = max(maxGain(node.right),0)#0表示不取该值
            self.maxSum = max(self.maxSum,node.val+leftGain+rightGain)#因为它本身也可能是一个负值
            return node.val + max(leftGain, rightGain)#因为从上一层看来，只有一边最后会被取到，因此只是选择了其中的最大值
        maxGain(root)
        return self.maxSum