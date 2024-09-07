# 如果直接调用链表来进行检查的话，每次都得从前往后找，会显得十分繁琐，因此我的思路是创建一个列表来对链表的值进行存储，然后用这个链表当中介来进行验证与比对。
# Definition for singly-linked list.
import queue


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
        '''方法一：存储于列表'''
        list_node = []
        while head:
            list_node.append(head.val)
            head = head.next
        for i in range(len(list_node)//2):
            if list_node[i] != list_node[-(i+1)]:
                return False
        return True
        '''方法二：使用栈,其实是错的，无法使用'''
        stack = queue.LifoQueue()
        if not head:
            return True
        stack.put(head.val)
        head = head.next
        while head:
            tem = stack.get()
            if tem != head.val:
                stack.put(tem)
                stack.put(head.val)
            head = head.next
        if stack.empty():
            return True
        else:
            return False
node_1 = ListNode(1,None)
node_2 = ListNode(2,None)
node_3 = ListNode(2,None)
node_4 = ListNode(1,None)
node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
solution = Solution()
print(solution.isPalindrome(node_1))