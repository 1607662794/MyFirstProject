# 注意：python 代码由 chatGPT🤖 根据我的 java 代码翻译，旨在帮助不同背景的读者理解算法逻辑。
# 本代码不保证正确性，仅供参考。如有疑惑，可以参照我写的 java 代码对比查看。

def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    n = len(gas)
    sum = 0
    for i in range(n):
        sum += gas[i] - cost[i]
    if sum < 0:
        # 总油量小于总的消耗，无解
        return -1
    # 记录油箱中的油量
    tank = 0
    # 记录起点
    start = 0
    for i in range(n):
        tank += gas[i] - cost[i]
        if tank < 0:
            # 无法从 start 到达 i + 1
            # 所以站点 i + 1 应该是起点
            tank = 0
            start = i + 1
    return 0 if start == n else start
