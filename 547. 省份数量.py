class UnionFind:
    def __init__(self):
        self.father = {}  # 存放着所有的相关关系，根节点的值为None
        self.num_of_sets = 0

    def find(self, x):  # 寻找根节点
        root = x  # 刚开始各位为营，大家都是各自的老大
        while self.father[root] != None:
            root = root.father
        while x != root:  # 路径压缩
            origin_father = self.father[x]
            self.father[x] = root
            x = origin_father
        return root

    def merge(self, x, y):  # 把x和y混合到一块儿
        root_x, root_y = self.find(x), self.find(y)

        if root_x != root_y:  # 两个没有关系的两个部落有了联系
            self.father[root_x] = root_y
            # 集合的数量-1
            self.num_of_sets -= 1

    def add(self, x):  # 添加根节点
        if x not in self.father:
            self.father[x] = None
            # 集合的数量+1
            self.num_of_sets += 1


class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        # 华为并查集
        uf = UnionFind()  # 只有一个并交集
        for i in range(len(isConnected)):
            uf.add(i)
            for j in range(i):
                if isConnected[i][j]:
                    uf.merge(i, j)
