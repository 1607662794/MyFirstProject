#力扣使用的是双指针法，小于x节点放在小指针处，大于x的节点放在大指针处，最后将两个链表连接起来。我的解法有点儿繁琐
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        add_node = ListNode()
        add_node.next = head#需要添加一个虚拟头结点，以便统一化操作
        #首先遍历链表节点，找到特定值前面的目标值节点
        fore_key_node = add_node
        current_node = add_node
        flag = True
        while current_node.next != None:
            if current_node.next.val >= x and current_node.next.next != None:
                fore_key_node = current_node
                flag = False
                break
            current_node = current_node.next
        if flag:
            return add_node.next#如果x节点前的所有节点都是小的，那么就不用移动，也不用遍历，直接返回

        #再次遍历一遍节点，将小于x值的节点移动到之前的关键节点前
        fore_current_node = fore_key_node.next
        while fore_current_node.next != None:
            if fore_current_node.next.val < x:
                tem_node = fore_current_node.next
                fore_current_node.next = fore_current_node.next.next#将小节点断开
                tem_node.next = fore_key_node.next
                fore_key_node.next = tem_node#将当前节点插入到关键节点前
                fore_key_node = fore_key_node.next#此时的关键节点也需要向后推移一位
                continue#交换后，重新看当前节点的值，因为后一个节点变了，所以不需要往后移动
            fore_current_node = fore_current_node.next
        return add_node.next

node_7 = ListNode(2,None)
node_6 = ListNode(5,node_7)
node_5 = ListNode(2,node_6)
node_4 = ListNode(0,node_5)
node_3 = ListNode(3,node_4)
node_2 = ListNode(4,node_3)
node_1 = ListNode(1,node_2)
solution = Solution()
print(solution.partition(node_1,3).next.val)

