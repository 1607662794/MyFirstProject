# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self, root, depth):
        if not root:
            return
        if depth == len(result):
            result.append(root.val)
        depth += 1
        self.dfs(root.right, depth)
        self.dfs(root.left, depth)

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 我的思路是深度优先搜索
        global result
        result = []
        self.dfs(root, 0)
        return result



