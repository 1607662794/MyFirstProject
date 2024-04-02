# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 我的思路是使用递归
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 1

        def find(node, depth):  # 返回当前层深度，其实这个depth也是可以删除掉的，只需要在max函数处多加1即可。
            if node == None:
                return depth
            else:
                return max(find(node.left, depth + 1), find(node.right, depth + 1))

        return find(root, depth) - 1

node_1 = TreeNode(3)
node_2 = TreeNode(9)
node_3 = TreeNode(20)
node_4 = TreeNode(15)
node_5 = TreeNode(7)
node_1.left = node_2
node_1.right = node_3
node_3.left = node_4
node_3.right = node_5

solution = Solution()
print(solution.maxDepth(node_1))

