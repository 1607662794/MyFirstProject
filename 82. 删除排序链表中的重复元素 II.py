#我的思路是采用双指针，第一个指针指向当前需要排查的节点，第二个指向当前节点，当第二个指针检查完所有的节点即排除所有重复节点
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
        #因为第一个指针是指向当前排除元素的上一个节点，因此对应于第二个指针到达最后一个元素的情况
        # 另外因为头结点可能不会保留，因此新建一个新的虚拟头节点来避免这种情况，
        suppositional_node = ListNode('a',head)
        fore_node = suppositional_node
        tail_node = suppositional_node
        while tail_node.next != None:
            if tail_node.next.val != tail_node.val and (tail_node.next.next != None and tail_node.next.val != tail_node.next.next.val or tail_node.next.next == None):#对应正常跳跃的情况，跳跃后到达数字元素
                fore_node.next = tail_node.next
                fore_node = fore_node.next
            elif tail_node.next.next == None and tail_node.val == tail_node.next.val:#对应第一个指针跳往None
                fore_node.next = None
            tail_node = tail_node.next
        return suppositional_node.next

node_4 = ListNode(4,None)
node_3 = ListNode(2,node_4)
node_2 = ListNode(2,node_3)
node_1 = ListNode(1,node_2)
print(node_1.next.val)
solution = Solution()
print(solution.deleteDuplicates(node_1).val)
