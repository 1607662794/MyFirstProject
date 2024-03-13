# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 我的思路是不断断开遍历过程中的节点，然后保存这个节点的下一节点，最后将这一节点的指向指向刚才的最后一个节点，因此需要三个指针来分别控制断开节点之前，断开节点，以及断开节点之后的部分。
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        first_node = ListNode()
        second_node = ListNode()
        third_node = ListNode()
        first_node.next = second_node
        second_node.next = third_node
        third_node.next = head
        while third_node:
            second_node.next = first_node
            first_node = second_node
            second_node = third_node
            third_node = third_node.next
            if first_node == head:  # 链表元素大于等于2
                first_node.next = None
        second_node.next = first_node
        return second_node


# node_5 = ListNode(5,None)
# node_4 = ListNode(4,node_5)
# node_3 = ListNode(3,node_4)
# node_2 = ListNode(2,node_3)
# node_1 = ListNode(1,node_2)

# node_1 = None

# node_2 = ListNode(2, None)
# node_1 = ListNode(1, node_2)

node_1 = ListNode(1, None)
solution = Solution()
print(solution.reverseList(node_1).val)
