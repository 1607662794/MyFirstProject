class Trie(object):
    #我的思路：一是建立一个列表，用于存储字符串，二是建立一个树形结构，用于存储前缀。
    # 我观察了一下官方题解，对方主要是使用了一个树结构（通过递归实现）和一个状态变量来表明是否是之前字符串的结束位置。
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        current_node = self
        for i in word:
            if not current_node.children[ord(i)-ord('a')]:
                current_node.children[ord(i)-ord('a')] = Trie()
            current_node = current_node.children[ord(i)-ord('a')]
        current_node.isEnd = True#只是停留在了当前节点处，还并没有继续下沉

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        current_node = self
        for i in word:
            if not current_node.children[ord(i)-ord('a')]:
                return False
            current_node = current_node.children[ord(i)-ord('a')]
        return current_node is not None and current_node.isEnd

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        current_node = self
        for i in prefix:
            if not current_node.children[ord(i)-ord('a')]:
                return False
            current_node = current_node.children[ord(i)-ord('a')]
        return current_node is not None



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)