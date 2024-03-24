def levenshtein_distance(text1, text2):
    """
    计算两个文本之间的编辑距离

    Args:
        text1: 文本1
        text2: 文本2

    Returns:
        编辑距离
    """

    # 将文本转换为列表
    text1_list = list(text1)
    text2_list = list(text2)

    # 创建一个二维矩阵，用于存储编辑距离
    distance_matrix = [[0 for _ in range(len(text2_list) + 1)] for _ in range(len(text1_list) + 1)]

    # 初始化第一行和第一列
    for i in range(len(text1_list) + 1):
        distance_matrix[i][0] = i
    for j in range(len(text2_list) + 1):
        distance_matrix[0][j] = j

    # 计算编辑距离
    for i in range(1, len(text1_list) + 1):
        for j in range(1, len(text2_list) + 1):
            if text1_list[i - 1] == text2_list[j - 1]:
                cost = 0
            else:
                cost = 1

            distance_matrix[i][j] = min(
                distance_matrix[i - 1][j] + 1,  # 删除
                distance_matrix[i][j - 1] + 1,  # 插入
                distance_matrix[i - 1][j - 1] + cost,  # 替换
            )

    # 返回编辑距离
    return distance_matrix[len(text1_list)][len(text2_list)]


# 示例
text1 = "雅诗兰黛（Estee Lauder） 雅诗兰黛眼霜肌透修护眼部精华霜小棕瓶眼霜 ANR眼霜15ml"
text2 = "雅诗兰黛（Estee Lauder）肌透修护眼部精华霜 15ml（眼霜 ANR 提拉紧致 淡化细纹 黑眼圈）"

distance = levenshtein_distance(text1, text2)

print(distance)
