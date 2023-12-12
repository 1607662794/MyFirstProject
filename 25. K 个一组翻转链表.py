# Definition for singly-linked list.
# 这道题主要看一下怎样实现链表的翻转
# 我的思路是，用列表将所有的链表节点均保存一遍，然后进行翻转化的的赋值，这样避免了重复链表中节点的找寻。
# 其中有两个循环，一个是k内的循环，用于交换k内的节点，另一个是确定进行几组k的交换
#我看力扣里面有一个尾插法思路挺巧的。
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverse_linklist(self, head, k):
        """注意，这里面的head指的是每k个节点组成的子链表，该函数的功能实现在于子链表的翻转"""
        saved_list = []
        fore_node = head
        for i in range(k):
            saved_list.append(head.val)
            head = head.next
        head = fore_node
        for i in range(k):
            head.val = saved_list[k - i - 1]
            head = head.next

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        length = 0
        fore_node = head

        while head != None:  # 判断输入链表有多长
            length += 1
            head = head.next

        head = fore_node

        for i in range(length // k):
            self.reverse_linklist(head, k)
            for _ in range(k):
                head = head.next

        return fore_node


solution = Solution()
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b
b.next = c
c.next = d
d.next = None
print(solution.reverseKGroup(a, 2).next.val)
