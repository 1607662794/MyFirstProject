# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# 使用快慢指针的思路
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return False

        quick_node = head.next.next
        slow_node = head.next
        while quick_node and quick_node.next:
            if quick_node == slow_node:
                return True
            else:
                quick_node = quick_node.next.next
                slow_node = slow_node.next
        return False


node_2 = ListNode(2)
node_1 = ListNode(1)
node_2.next = None
node_1.next = node_2
solution = Solution()
print(solution.hasCycle(node_1))