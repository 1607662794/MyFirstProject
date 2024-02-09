#我的思路是遍历一遍所有元素，如果发现存在重复元素，则删除下一个元素，这道题可以采用单指针进行，上一道题因为要删除元素本身，所以采用双指针进行。
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        current_node = head
        while current_node.next != None:
            if current_node.val == current_node.next.val and current_node.next.next != None:
                current_node.next = current_node.next.next
            elif current_node.val == current_node.next.val and current_node.next.next == None:
                current_node.next = None
            current_node = current_node.next
        return head

node_4 = ListNode(4,None)
node_3 = ListNode(2,node_4)
node_2 = ListNode(2,node_3)
node_1 = ListNode(1,node_2)
solution = Solution()
print(solution.deleteDuplicates(node_1).next.next.val)
