# 我的思路是，任何一个节点可能既作为一棵树中的左子树节点，也作为一棵树中的右子树节点，而正是因为它所在的这种位置关系，框定了它的取值范围。
# 我刚开始的思路错误的一个原因在于，树的边上其实并不是一个闭区间，而是半开半闭区间
# 因此可以利用二叉树的中序搜索来进行检查，也不一定需要再定义一个列表进行存储，只需要一个变量进行前后对比即可。
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        result = []
        def backtracking(root):
            if root == None:
                return
            elif root.left == None and root.right == None:  # 中间三个判断条件其实可以去掉的，因为最后一个条件已经包含了这几种情况。
                result.append(root.val)
            elif root.left != None and root.right == None:
                backtracking(root.left)
                result.append(root.val)
            elif root.left == None and root.right != None:
                result.append(root.val)
                backtracking(root.right)
            elif root.left != None and root.right != None:
                backtracking(root.left)
                result.append(root.val)
                backtracking(root.right)

        backtracking(root)

        for i in range(len(result) - 1):
            if result[i] >= result[i+1]:
                return False
        return True
