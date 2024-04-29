class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的
class Solution:
    def mergeTwoLists(self, l1, l2) :
        # write code here
        # current_node_1 = l1
        # current_node_2 = l2
        # merge = ListNode(0)
        # while True:
        #     if current_node_1 and current_node_2:
        #         if current_node_1.val < current_node_2.val:
        #             merge.next = current_node_1
        #         else:
        #             merge.next = current_node_2
        #     if not current_node_1 and current_node_2:
        #         while current_node_2:
        #             merge.next = current_node_2
        #
        if not l1:
            return l2
        elif not l2:
            return l1
        else:
            list_1 = []
            list_2 = []
            while l1:
                list_1.append(l1.val)
                l1 = l1.next
            while l2:
                list_2.append(l2.val)
                l2 = l2.next
            merge_list = list_2 + list_1
            merge_list = sorted(merge_list)
            merge_node = ListNode(0)
            current_node = merge_node
            for i in merge_list:
                current_node.next = ListNode(i)
                current_node = current_node.next
            return merge_node.next
node_1 = ListNode(1)
node_4 = ListNode(4)
node_6 = ListNode(6)
node_2 = ListNode(2)
node_3 = ListNode(3)
node_5 = ListNode(5)
node_1.next = node_4
node_4.next =node_6
node_2.next = node_3
node_3.next = node_5
solution = Solution()
print(solution.mergeTwoLists(node_1,node_2).val)

