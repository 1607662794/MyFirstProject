# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def creat_linklist_tail(li):  # 将输入的列表，每个元素按照尾插的方式插入链表尾端
    tail = ListNode(li[0])
    head = tail
    for element in li[1:]:
        tail.next = ListNode(element)
        tail = ListNode(element)
    return head


head = creat_linklist_tail([1, 2, 3, 4, 5])


# print(head.val)

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        num = 0
        target = head

        # 计算链表总长度
        while target != None:
            num += 1
            target = target.next
        target = head

        # 定位删除点的上一位
        if n == 1:  # 这种情况下是删除最后一个节点
            if num == 1:  # 此时的链表是空的
                return None
            else:
                for number in range(num - n - 1):
                    target = target.next
                target.next = None
        elif n == num:  # 头结点需要改变，题解中提供了一个思路是，在原有链表的基础上，创建一个哑节点，这样的话，原来的头节点就不是头节点了
            head = head.next
        else:  # 这种情况下，是跳跃了某个节点
            for number in range(num - n - 1):
                target = target.next
            target.next = target.next.next

        # 返回头结点
        return head


a = Solution()
print(a.removeNthFromEnd(head=head, n=2).next.val)
