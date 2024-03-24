import collections

# 定义存储 key 对应 value 数量的字典
key_value_count = collections.defaultdict(dict)#默认返回一个集合

# 定义存储 value 出现次数的字典，最后再通过索引合起来
value_count = collections.Counter()

# 遍历文本文件
with open("input.txt", "r") as f:
    for line in f:
        # 分割 key 和 value
        key, value = line.strip().split("\t")

        # 统计 key 对应 value 的数量
        key_value_count[key][value] = key_value_count[key].get(value, 0) + 1

        # 统计 value 出现次数
        value_count[value] += 1

# 按 value 出现次数从大到小排序
sorted_value_count = sorted(value_count.items(), key=lambda x: x[1], reverse=True)

# 输出结果文件
with open("output.txt", "w") as f:
    for key, value_counts in key_value_count.items():
        # 将 key 对应 value 数量格式化为字符串
        value_str = ";".join(f"{value},{count}" for value, count in value_counts.items())

        # 输出结果
        f.write(f"{key}:{value_str}\n")

