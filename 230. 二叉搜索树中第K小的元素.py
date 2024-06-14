# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []  # 用栈的形式遍历所有节点
        while root or stack:
            while root:  # 从当前节点往左下方溜
                stack.append(root)
                root = root.left
            root = stack.pop()  # 遍历的当前节点
            k = k - 1
            if k == 0:
                return root.val
            root = root.right





