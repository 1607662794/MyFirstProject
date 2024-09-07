# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):  # 广度有限搜索
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if root:
            cur_list = [root]
        else:
            return result
        while cur_list:
            result.append([])
            next_list = []
            for i in cur_list:
                if i:  # 检查当前层，并添加当前层数值
                    result[-1].append(i.val)
                if i.left:
                    next_list.append(i.left)
                if i.right:
                    next_list.append(i.right)
            cur_list = next_list
        return result

