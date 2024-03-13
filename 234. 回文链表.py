# 如果直接调用链表来进行检查的话，每次都得从前往后找，会显得十分繁琐，因此我的思路是创建一个列表来对链表的值进行存储，然后用这个链表当中介来进行验证与比对。
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        list_node = []
        while head:
            list_node.append(head.val)
            head = head.next
        for i in range(len(list_node)//2):
            if list_node[i] != list_node[-(i+1)]:
                return False
        return True
node_1 = ListNode(1,None)
solution = Solution()
print(solution.isPalindrome(node_1))