# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root.left and root.right:
            return self.isequal(root.left,root.right)
        elif not root.left and not root.right:
            return True
        else:
            return False
    def isequal(self,left_node,right_node):
        if left_node and right_node and left_node.val == right_node.val:
            return self.isequal(left_node.right,right_node.left) and self.isequal(left_node.left,right_node.right)
        elif not left_node and not right_node:
            return True
        else:
            return False