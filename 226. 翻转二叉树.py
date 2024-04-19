# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        elif root.right or root.left:
            root.right, root.left = root.left,root.right
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root

node_1 = TreeNode(2)
node_2 = TreeNode(1)
node_3 = TreeNode(3)
node_1.left = node_2
# node_1.right = node_3
solution = Solution()
print(solution.invertTree(node_1).val)

