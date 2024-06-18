# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.pre = None
        def dfs(root):
            if root == None:
                return None
            dfs(root.right)
            dfs(root.left)
            root.right =self.pre
            root.left = None
            self.pre = root
        dfs(root)
node_1 = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(3)
node_4 = TreeNode(4)
node_5 = TreeNode(5)
node_6 = TreeNode(6)
node_1.left = node_2
node_1.right = node_5
node_2.left = node_3
node_2.right = node_4
node_5.right=node_6
solution = Solution()
# print(solution.flatten(node_1))
node_1.val = 2
print(node_1.val)
