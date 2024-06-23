# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # 我的思路是后序遍历，只要查找到这两个节点后再遇到根节点，则返回该根节点
        # 终止条件为，碰到空节点，或者p或者q，因为对于最后的条件来说，如果当前节点的左右子树都返回了非空值
        # 则当前节点为最近祖先，如果当前节点为所求节点，那么如果它的左（右）子树返回了非空值，则该节点为最近祖先节点
        if root == None or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if left == None:
            return right
        elif right == None:
            return left
        else:
            return root

