# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 数学公式推导：a+n(b+c)+b=a+(n+1)b+nc。→ a=c+(n−1)(b+c) →因此，当发现 slow\textit{slow}slow 与 fast\textit{fast}fast 相遇时，我们再额外使用一个指针 ptr\textit{ptr}ptr。起始，它指向链表头部；随后，它和 slow\textit{slow}slow 每次向后移动一个位置。最终，它们会在入环点相遇。
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return None

        quick_node = head.next.next
        slow_node = head.next
        while quick_node and quick_node.next:
            if quick_node == slow_node:
                per = head
                while True:
                    if per == slow_node:
                        return per
                    else:
                        per = per.next
                        slow_node = slow_node.next
            else:
                quick_node = quick_node.next.next
                slow_node = slow_node.next
        return None


node_2 = ListNode(2)
node_1 = ListNode(1)
node_2.next = None
node_1.next = node_2
solution = Solution()
print(solution.hasCycle(node_1))