# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        # 对于这道题，我的思路是回溯，我原本在想按照层次遍历的方式进行动态规划，但是每一层有不同的节点，如果非要
        # 使用动态规划的话，得是一个三维矩阵
        # 所以使用前缀和+回溯
        self.num = 0

        def backtrace(root, prefix):  # prefix代表当前节点的前缀和
            if not root:
                return
            prefix.append(prefix[-1] + root.val)
            if prefix[-1] - targetSum in prefix[:-1]:  # 是查看当前节点之前的前缀和是否有满足要求的，因此不需要查看最后一个值。
                self.num += prefix[:-1].count(prefix[-1] - targetSum)  # 这儿也可以用官方题解，字典的形式。
            backtrace(root.left, prefix)
            backtrace(root.right, prefix)
            prefix.pop()  # 回溯法记得还原。

        backtrace(root, [0])  # 第一个零，既是为了列表的完整性，同时也是代表取当前节点等于求和值的情况。
        return self.num

