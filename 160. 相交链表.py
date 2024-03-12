# Definition for singly-linked list.
# Leecode的思路比较巧妙
# 如果两个链表相交，那么相交点之后的长度是相同的
#
# 我们需要做的事情是，让两个链表从同距离末尾同等距离的位置开始遍历。这个位置只能是较短链表的头结点位置。
# 为此，我们必须消除两个链表的长度差
#
# 指针 pA 指向 A 链表，指针 pB 指向 B 链表，依次往后遍历
# 如果 pA 到了末尾，则 pA = headB 继续遍历
# 如果 pB 到了末尾，则 pB = headA 继续遍历
# 比较长的链表指针指向较短链表head时，长度差就消除了
# 如此，只需要将最短链表遍历两次即可找到位置
# 听着可能有点绕，看图最直观，链表的题目最适合看图了
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # while headA:
        #     headB_copy = headB
        #     while headB_copy:
        #         if headA == headB_copy:
        #             return headA
        #         headB_copy = headB_copy.next
        #     headA = headA.next
        # return None
        Pa = headA
        Pb = headB
        while True:
            if Pb == None and Pa != None:#第一遍遍历
                Pb = headA
                while Pa:
                    Pb = Pb.next
                    Pa = Pa.next
                Pa = headB
                while Pa:
                    if Pa == Pb:
                        return Pa
                    else:
                        Pb = Pb.next
                        Pa = Pa.next
                return None
            elif Pa == None and Pb != None:
                Pa = headB
                while Pb:
                    Pb = Pb.next
                    Pa = Pa.next
                Pb = headA
                while Pa:
                    if Pa == Pb:
                        return Pa
                    else:
                        Pb = Pb.next
                        Pa = Pa.next
                return None
            elif Pa == Pb:
                return Pa
            else:
                Pb = Pb.next
                Pa = Pa.next


