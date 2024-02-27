# 这道题的思路是直接看的LeeCode
# 假设 n 个节点存在二叉排序树的个数是 G (n)，令 f(i) 为以 i 为根的二叉搜索树的个数，则
# G(n)=f(1)+f(2)+f(3)+f(4)+...+f(n)G(n) = f(1) + f(2) + f(3) + f(4) + ... + f(n)G(n)=f(1)+f(2)+f(3)+f(4)+...+f(n)

# 当 i 为根节点时，其左子树节点个数为 i-1 个，右子树节点为 n-i，则
# f(i)=G(i−1)∗G(n−i)f(i) = G(i-1)*G(n-i)f(i)=G(i−1)∗G(n−i)

# 综合两个公式可以得到 卡特兰数 公式
# G(n)=G(0)∗G(n−1)+G(1)∗(n−2)+...+G(n−1)∗G(0)G(n) = G(0)*G(n-1)+G(1)*(n-2)+...+G(n-1)*G(0)G(n)=G(0)∗G(n−1)+G(1)∗(n−2)+...+G(n−1)∗G(0)

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        G = [0] * (n+1)
        G[0] = 1
        G[1] = 1
        for i in range(2,n+1):
            for j in range(1,i+1):
                G[i] += G[j-1]*G[i-j]
        return G[n]
