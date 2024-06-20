class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.capacity_list = []  # 用于顺序存储最新的关键字
        self.lru = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.lru.get(key) != None:
            self.capacity_list.remove(key)  # 涉及之后需要更新最新序列,列表是有序的，所以我在这儿花费了时间。
            self.capacity_list.append(key)
            return self.lru[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.lru.get(key) != None:
            self.lru[key] = value
            self.capacity_list.remove(key)  # 更改之后需要更新最新序列
            self.capacity_list.append(key)
        else:
            self.lru[key] = value
            self.capacity_list.append(key)
            if len(self.capacity_list) > self.capacity:
                del self.lru[self.capacity_list[0]]
                self.capacity_list.pop(0)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)