# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        # 该题为华为题库递归
        if root == None:  # 因为空节点其实对应的是无值的状态而不是为零的状态，所以单独考虑。
            return False
        elif root.left == None and root.right == None:
            return targetSum == root.val
        else:
            targetSum = targetSum - root.val
            return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)


node = TreeNode()
solution = Solution()
print(solution.hasPathSum(node, 0))
