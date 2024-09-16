# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """

        def find_mid(node):
            # 寻找中间的节点，对于偶数，返回中间偏左的那个节点；对于奇数，返回中间的那个节点。
            fast = node
            slow = node
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            return slow

        def reversed_list(node):
            '''返回翻转后链表的新头结点'''
            pre_node = None
            while node:
                tem = node.next
                node.next = pre_node
                pre_node = node
                node = tem
            return pre_node

        def join_list(list_A, list_B):
            '''左节点大于等于右节点链表长度'''
            dummy_node = ListNode(0)
            cur_node = dummy_node
            while True:
                cur_node.next = list_A
                cur_node = cur_node.next
                if not cur_node:
                    break
                list_A = list_A.next
                cur_node.next = list_B
                cur_node = cur_node.next
                if not cur_node:
                    break
                list_B = list_B.next
            return dummy_node.next

        mid_node = find_mid(head)
        list_1 = head
        list_2 = mid_node.next
        mid_node.next = None
        list_2 = reversed_list(list_2)
        return join_list(list_1, list_2)

node_5 = ListNode(5, None)
node_4 = ListNode(4, node_5)
node_3 = ListNode(3, node_4)
node_2 = ListNode(2, node_3)
node_1 = ListNode(1, node_2)
solution = Solution()
print(solution.reorderList(node_1).val)

