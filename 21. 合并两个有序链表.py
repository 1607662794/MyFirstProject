# Definition for singly-linked list.
# 本题的思路是：利用链表的性质，首先先定位一个头结点，然后使最后生成的链表依次往后滑，不断生成与新增，对于链表1和2的判断，采用两个头节点，每次小的或者另外一个链表已经到达末尾后，链表的头指针依次往后滑，列表同理
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        merge = ListNode()
        merge_head = merge
        while list1 != None or list2 != None:
            if list2 == None or (list1 != None and list1.val < list2.val):  # 逻辑运算如果前面的判断结果已经能够决定最后的判断结果的话，不需要进行后续的计算
                merge.next = ListNode(list1.val)
                merge = merge.next
                list1 = list1.next
            else:
                merge.next = ListNode(list2.val)
                merge = merge.next
                list2 = list2.next
        return merge_head.next


solution = Solution()
# s = ListNode()
a = ListNode(1)
b = ListNode(2)
c = ListNode(4)
# s.next = a
a.next = b
b.next = c
d = ListNode(1)
e = ListNode(3)
f = ListNode(4)
d.next = e
e.next = f
# print(s.next.val)
print(solution.mergeTwoLists(a, d).next.next.next.next.next.val)
