# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []

        def recursion(root):
            if root == None:
                return
            elif root.left == None and root.right == None:  # 中间三个判断条件其实可以去掉的，因为最后一个条件已经包含了这几种情况。
                result.append(root.val)
            elif root.left != None and root.right == None:
                recursion(root.left)
                result.append(root.val)
            elif root.left == None and root.right != None:
                result.append(root.val)
                recursion(root.right)
            elif root.left != None and root.right != None:
                recursion(root.left)
                result.append(root.val)
                recursion(root.right)

        recursion(root)
        return result


p = TreeNode()
p.val = 1
# p.left = TreeNode()
# p.left.val = 2
p.right = TreeNode()
p.right.val = 2
p.right.left = TreeNode()
p.right.left.val = 3

# q = TreeNode()
# q.val = 1
# # q.left = TreeNode()
# # q.left.val = 2
# q.right = TreeNode()
# q.right.val = 2

solution = Solution()
print(solution.inorderTraversal(p))
