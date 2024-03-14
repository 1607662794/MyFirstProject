class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

# 这道题可以使用哈希表来进行解决，原链表当做key来进行存储，新链表当做value来进行存储。
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
            # 创建一个哈希表，key是原节点，value是新节点
        d = dict()
        p = head
        # 将原节点和新节点放入哈希表中
        while p:
            new_node = Node(p.val, None, None)
            d[p] = new_node
            p = p.next
        p = head
        # 遍历原链表，设置新节点的next和random
        while p:
            # p是原节点，d[p]是对应的新节点，p.next是原节点的下一个
            # d[p.next]是原节点下一个对应的新节点
            if p.next:
                d[p].next = d[p.next]
            # p.random是原节点随机指向
            # d[p.random]是原节点随机指向  对应的新节点
            if p.random:
                d[p].random = d[p.random]
            p = p.next
        # 返回头结点，即原节点对应的value(新节点)
        return d[head]