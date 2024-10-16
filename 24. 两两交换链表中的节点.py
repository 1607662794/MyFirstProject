# Definition for singly-linked list.对于这道题我的思路是制定一个循环，然后每两个进行一次交换，得到最后交换节点
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # fore_node = head
        # flag = 0
        # while head != None and head.next != None:
        #     if flag % 2 == 0:
        #         value = head.val
        #         head.val = head.next.val
        #         head.next.val = value
        #     head = head.next
        #     flag += 1
        # return fore_node
        flag = 0
        dummy_node = List
        current_node = head
        while current_node:
            flag += 1
            if flag % 2 != 0:
                first_node = current_node
            else:
                second_node = current_node
                first_node.next = second_node.next
                second_node.next = first_node
            current_node = current_node.next
        return head



solution = Solution()
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b
b.next = c
c.next = d
d.next = None
print(solution.swapPairs(a).val)
