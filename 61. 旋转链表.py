# 我的思路是，首先定位移动到的位置，然后将这个点给断开，将之前的首尾相连，并用超过一个周期长度的移动位数进行折减来增加速度
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return None
        number = 1  # 首先遍历一遍，查询整个链表的长度，不然不知道该截断的位置具体在哪儿
        current_node = head
        while current_node.next != None:
            number += 1
            current_node = current_node.next
        current_node.next = head  # 把尾节点与头结点相连
        current_node = head
        k = k % number
        for i in range(number - k - 1):
            current_node = current_node.next
        head = current_node.next
        current_node.next = None  # 把新的头结点前的链表断开
        return head


solution = Solution()
print(solution.rotateRight())
