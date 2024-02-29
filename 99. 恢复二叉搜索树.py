# 对于这道题我还是没有什么思路，我的初步想法是，找到一个异常的值简单，但是找到另一个需要交换的节点我就一时想不到了
# 看了LeeCode的解法后，发现其实中序遍历的条件下，需要交换的两个节点是相连的，这样就解决了另一个交换点难以寻找的问题。
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # 用两个变量x，y来记录需要交换的节点
        self.x = None
        self.y = None
        self.pre = None

        # 中序遍历二叉树，并比较上一个节点(pre)和当前节点的值，如果pre的值大于当前节点值，则记录下这两个节点
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            if not self.pre:
                self.pre = root
            else:
                if self.pre.val > root.val:
                    self.y = root
                    if not self.x:
                        self.x = self.pre
                self.pre = root
            dfs(root.right)

        dfs(root)
        # 如果x和y都不为空，说明二叉搜索树出现错误的节点，将其交换
        if self.x and self.y:
            self.x.val, self.y.val = self.y.val, self.x.val

