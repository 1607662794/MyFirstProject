import numpy as np

# 定义输入数据
input_data = np.array([1, 2, 3, 4, 5])

# 定义输出数据
output_data = np.array([2, 4, 6, 8, 10])

# 计算系数
w = np.dot(output_data, input_data) / np.dot(input_data, input_data)
b = np.mean(output_data) - w * np.mean(input_data)

# 预测新值
new_input = 6

new_output = w * new_input + b

print(new_output)
