# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#从前序或者后序，结合中序可以实现二叉树的复原。
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        # 把它当做一个树串下来的子树就可以。
        def build_root(preorder_left, preorder_right, inorder_left, inorder_right):  # 返回当前构造的根节点
            if preorder_left > preorder_right:
                return None
            inorder_index = index[preorder[preorder_left]]
            tree_node = TreeNode(preorder[preorder_left])
            left_distance = inorder_index - inorder_left
            tree_node.left = build_root(preorder_left + 1, preorder_left + left_distance, inorder_left,
                                        inorder_index - 1)
            tree_node.right = build_root(preorder_left + left_distance + 1, preorder_right, inorder_index + 1,
                                         inorder_right)

            return tree_node

        length = len(preorder)
        index = {element: i for i, element in enumerate(inorder)}
        root = build_root(0, length - 1, 0, length - 1)
        return root



