# 我的思路是保持头结点对应的链表顺序始终不变，另外设置一个result_node节点用于结果的保存，就像基因序列里的复制一样！
# Leecode中的方法是单独设置了一个反转函数，该函数将链表掉个个，然后将顺序颠倒即可。
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        current_node = head
        result_head_node = ListNode()
        result_current_node = result_head_node
        for i in range(left - 1):  # 刚开始不需要反转的节点
            result_current_node.val = current_node.val  # 不能直接赋值，不然就会导致原列表变化，因为python的变量是引用。
            result_current_node.next = ListNode()  # 如果不定义下一个节点是链表节点的话，那么None是Nonetype类型，将无法赋值。
            result_current_node = result_current_node.next
            current_node = current_node.next
        flag = False
        for i in range(right - left + 1):  # 需要反转的节点，此时的current_node始终停留在反转节点的第一位
            tem_current_node = current_node
            j = right - left - i
            while j > 0:
                tem_current_node = tem_current_node.next
                j -= 1
            if tem_current_node.next == None:
                flag = True
            result_current_node.val = tem_current_node.val
            if right - left - i == 0 and flag:
                return result_head_node  # 仅仅result_current_node改变不会影响result_head_node的顺序。
            else:
                result_current_node.next = ListNode()
                result_current_node = result_current_node.next
        for i in range(right - left + 1):  # 前进current_node至不需要反转的节点
            current_node = current_node.next
        while current_node != None:  # 不需要反转的节点
            result_current_node.val = current_node.val
            if current_node.next == None:
                return result_head_node
            else:
                result_current_node.next = ListNode()
                result_current_node = result_current_node.next
                current_node = current_node.next
        return result_head_node


node_5 = ListNode(5, None)
node_4 = ListNode(4, node_5)
node_3 = ListNode(3, node_4)
node_2 = ListNode(2, node_3)
node_1 = ListNode(1, node_2)
solution = Solution()
print(solution.reverseBetween(node_1, 2, 4).val)
print(solution.reverseBetween(node_1, 2, 4).next.val)
print(solution.reverseBetween(node_1, 2, 4).next.next.val)
print(solution.reverseBetween(node_1, 2, 4).next.next.next.val)
print(solution.reverseBetween(node_1, 2, 4).next.next.next.next.val)
print(solution.reverseBetween(node_1, 2, 4).next.next.next.next.next)
