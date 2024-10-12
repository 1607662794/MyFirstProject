# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root):
        self.result = True
        def backtrace(node):
            if not node:
                return 0
            left_height = backtrace(node.left)
            right_height = backtrace(node.right)
            if abs(left_height-right_height) > 1:
                self.result = False
            return max(left_height,right_height)+1
        backtrace(root)
        return self.result
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(3)
root.left.left.left = TreeNode(4)
root.left.left.right = TreeNode(4)
solution = Solution()
print(solution.isBalanced(root))