# Definition for singly-linked list.
# 这道题主要看一下怎样实现链表的翻转
# 我的思路是，用列表将所有的链表节点均保存一遍，然后进行翻转化的的赋值，这样避免了重复链表中节点的找寻。
# 其中有两个循环，一个是k内的循环，用于交换k内的节点，另一个是确定进行几组k的交换
#我看力扣里面有一个尾插法思路挺巧的。
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head, k):
        number = 0
        dummy = ListNode(0, head)
        pre = dummy
        left = head
        while head:
            number += 1
            if number % k == 0:
                tem = head.next
                left, right = self.reverse(left, head, k)
                pre.next = left
                pre = right
                head = tem
                left = head
                right.next = head
            else:
                head = head.next
        return dummy.next

    def reverse(self, left, right, k):
        head = None
        current_node = left
        for i in range(k):
            tem = current_node.next
            current_node.next = head
            head = current_node
            current_node = tem
        return (right, left)


solution = Solution()
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b
b.next = c
c.next = d
d.next = None
print(solution.reverseKGroup(a, 2))
