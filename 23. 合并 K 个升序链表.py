# Definition for singly-linked list.目前的这种做法，我是使用提取，然后排序，最后在转换为链表，时间复杂度为nlogn+2n，我刚想到了一种新的方法，就是使用堆的概念，每次只比较每个链表最低端的几个数，然后插入链表，这样时间复杂度只有n，我可真是一个天才
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        merge_listnode = ListNode()
        fore_node = merge_listnode
        merge_list = []
        for i in lists:
            while i != None:
                merge_list.append(i.val)
                i = i.next
        merge_list.sort()
        for i in merge_list:
            current_node = ListNode(i)
            merge_listnode.next = current_node
            merge_listnode = current_node
        return fore_node.next

solution = Solution()
a = ListNode(1)
b = ListNode(4)
c = ListNode(5)
a.next = b
b.next = c
c.next = None
print(solution.mergeKLists([a]).next.val)


