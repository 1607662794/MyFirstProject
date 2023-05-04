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
        # 使用递归进行不断地拆分求和

        # 肯定得至少一位数字相加，不然没有了意义
        num = l1.val + l2.val
        l = ListNode(num % 10, None)
        # 注意，空列表并不为None值，因此需要提取其布尔值进行运算
        # 这个循环判断排除掉了其余的三种情况
        while (l1 == l2 and l1 == None) is False:
            # 对不同位数字相加所做的准备
            if l1 == None and l2 != None:
                l1.next(0)
            elif l2 == None and l1 != None:
                l2.next(0)
            else:
                # 构造进位和不进位的操作
                if num > 9:
                    tag = 1
                else:
                    tag = 0
                num = l1.val + l2.val + tag
                l.next(num % 10)

            if num > 9:
                l.next(1)
            return l

        return l




node3 = ListNode(3,None)
node2 = ListNode(4,node3)
node1 = ListNode(2,node2)
node6 = ListNode(4,None)
node5 = ListNode(6,node6)
node4 = ListNode(5,node5)

print(node1.val)
a = Solution()
print(a.addTwoNumbers(node1, node4))
