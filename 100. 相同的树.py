# 注意，这里的判断相等与否时，判断的是引用的地方是否相同，而带括号的类实例是相当于类实例化了，也就是目标地址并不一样。
# 因为一个分支检查完后要回溯到根节点，然后抵达右子节点，这时候可以在分支的时候做一个并列的判断。
# 要先检查完None值后再判断非None的情况。
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q != None or p != None and q == None :
            return False
        elif p == None and q == None or p.val == q.val and p.left == None and p.right == None and q.left == None and q.right == None:
            return True
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


p = TreeNode()
p.val = 1
# p.left = TreeNode()
# p.left.val = 2
# p.right = TreeNode()
# p.right.val = 3

q = TreeNode()
q.val = 1
# q.left = TreeNode()
# q.left.val = 2
q.right = TreeNode()
q.right.val = 2

solution = Solution()
print(solution.isSameTree(p, q))
