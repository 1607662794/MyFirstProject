# 换个角度考虑，就是从起点出发，看看能够到达的区域大小
class Solution:
    def apply(self, generated_map):
        self.seek_area = 0
        # write code here
        x = len(generated_map)
        y = len(generated_map[0])
        area = x * y
        # 为迷宫外围添加一层墙，减轻判断条件的工作量
        generated_map.insert(0, [1 for i in range(y)])
        generated_map.append([1 for i in range(y)])
        for i in range(len(generated_map)):
            generated_map[i].insert(0, 1)
            generated_map[i].append(1)

        def seek(i, j):  # 如果设置return的话，将会是深度优先搜索，提前结束，所以我设置为这个样子用来完全搜索。
            self.seek_area += 1
            generated_map[i][j] = 2
            if generated_map[i - 1][j] == 0:
                seek(i - 1, j)
            if generated_map[i + 1][j] == 0:
                seek(i + 1, j)
            if generated_map[i][j - 1] == 0:
                seek(i, j - 1)
            if generated_map[i][j + 1] == 0:
                seek(i, j + 1)
            # if (generated_map[i - 1][j] == 1 or generated_map[i - 1][j] == 2) and (
            #         generated_map[i + 1][j] == 1 or generated_map[i + 1][j] == 2) and (
            #         generated_map[i][j - 1] == 1 or generated_map[i][j - 1] == 2) and (
            #         generated_map[i][j + 1] == 1 or generated_map[i][j + 1] == 2):  # 终止条件，
            #     return seek_area  # 表示已经探查过的区域

        seek(1, 1)
        return area - self.seek_area


solution = Solution()
print(solution.apply([[0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [1, 0, 0, 0]]))
