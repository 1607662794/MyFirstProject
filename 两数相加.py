class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''第一种方法基于列表实现'''


class Solution_list(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 使用递归进行不断地拆分求和
        l = []
        # 肯定得至少一位数字相加，不然没有了意义
        num = l1.pop(0) + l2.pop(0)
        l.append(num % 10)
        # 注意，空列表并不为None值，因此需要提取其布尔值进行运算
        # 这个循环判断排除掉了其余的三种情况
        while (l1 == l2 and bool(l1) is False) is False:
            # 对不同位数字相加所做的准备
            if bool(l1) is False and bool(l2) is not False:
                l1.append(0)
            elif bool(l2) is False and bool(l1) is not False:
                l2.append(0)
            else:
                # 构造进位和不进位的操作
                if num > 9:
                    tag = 1
                else:
                    tag = 0
                num = l1.pop(0) + l2.pop(0) + tag
                l.append(num % 10)
        if num > 9:
            l.append(1)
        return l


'''第二种方法基于链表实现'''


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # 判断是否是0位数字
        if l1 == None and l2 != None:
            return l2
        elif l2 == None and l1 != None:
            return l1
        # 判断是否是1位数字
        if l1.next == None and l2.next != None:
            l1.next = ListNode(0, None)
        elif l2.next == None and l1.next != None:
            l2.next = ListNode(0, None)
        num = l1.val + l2.val
        l1 = l1.next
        l2 = l2.next
        l = ListNode(num % 10, None)
        start = l

        # 使用递归进行不断地拆分求和
        # start的设置要求在递归外边，所以要求数字起码二位数相加
        while (l1 == l2 and l1 == None) is False:
            # 对不同位数字相加所做的准备
            if l1.next == None and l2.next != None:
                l1.next = ListNode(0, None)
            elif l2.next == None and l1.next != None:
                l2.next = ListNode(0, None)
            else:
                # 构造进位和不进位的操作
                if num > 9:
                    tag = 1
                else:
                    tag = 0
                num = l1.val + l2.val + tag
                l1 = l1.next
                l2 = l2.next
                l.next = ListNode(num % 10, None)
                l = l.next

        if num > 9:
            l.next = ListNode(1, None)
            l = l.next

        return start


node3 = ListNode(1, None)
node2 = ListNode(9, node3)
node1 = ListNode(9, node2)
# node6 = ListNode(1, None)
# node5 = ListNode(6, node6)
node4 = ListNode(1, None)

print(node1.next.val)
a = Solution()
print(a.addTwoNumbers(node1, node4).val)
