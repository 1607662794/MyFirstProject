# 该文档用于我练手的一些代码，包括字典排序，文件读取等。
import csv
import math
import os
import statistics
import time
from functools import reduce

import numpy as np
import pandas as pd
from tqdm import tqdm

# 时间函数
time_1 = time.time()

# # 目录地址
# print("当前文件工作路径", os.getcwd())
# print("当前文件地址", __file__)
# print("划分当前文件地址为后缀及文件名两部分", os.path.splitext(__file__)[0])
# print("划分当前文件地址为后缀及文件名两部分", os.path.splitext(__file__)[1])
# print("划分当前文件为后缀及文件名两部分", os.path.basename(__file__).split('.')[0])
# print("划分当前文件为后缀及文件名两部分", os.path.basename(__file__).split('.')[1])
# print("判断该文件是否存在", os.path.isfile(__file__))
# print("判断该路径是否存在", os.path.isdir(os.getcwd()))
# print("判断该路径是否存在(因为我加了文件名，所以会报错)", os.path.isdir(__file__))
# print("判断 path 对应文件或目录是否存在)", os.path.exists(__file__))
# print("合并路径{}".format(os.path.join("D:", "/Code/MyFirstProject/demo")))
# print("当前目录下的所有文件{}".format(os.listdir()))
# dir = [os.getcwd() + i for i in os.listdir(os.getcwd())]
# print("当前目录下的所有文件地址{}".format(dir))
#

# # 进度函数
# # for i in tqdm(os.listdir()):
# #     if i.split(".")[-1] == 'py':
# #         print(i)
# # print("\t")
#

# # 数学运算
# print("6/5向上取整；", math.ceil(6/5))
# print("6/5向下取整；", math.floor(6/5))
# print("6/5四舍五入；", round(6/5))

# # 常见操作
# print("字符串分割，括号内的形参可以指定个数","abc".split())
# print("单词分割为字母",list('abc'))
# print("字母合并为单词",''.join(['a','b','c']))
# print("移除字符串头头尾的指定字符，默认为空格，左删除为lstrip(),右删除为rstrip()","  Hello,World  ".strip())

# # 本机配置
# print("输出cpu的颗数", os.cpu_count())
#

# # 字符 →→ ASCII码
# print("1~9的ASCII分布：{}~{}".format(ord('1'), ord('9')))
# print("a~z的ASCII分布：{}~{}".format(ord('a'), ord('z')))
# print("A~Z的ASCII分布：{}~{}".format(ord('A'), ord('Z')))
#
# # 字符 →→ ASCII码
# print(chr(49))


# os读取文本txt
# with open("example.txt", "r") as file:
#     # r + 模式表示以读写模式打开文件。在这种模式下，您可以读取和写入文件，而不会清空文件内容。如果文件不存在，则会引发    FileNotFoundError    错误。
#     # w    模式表示以写入模式打开文件。在这种模式下，如果文件存在，则会清空文件内容并写入新的数据；如果文件不存在，则会创建新文件。因此，使用    w    模式会覆盖原始文件内容。
#     # #读取整个文件
#     # content = file.read() # 这样读取的话，所有的内容是连在一起的一个字符串，不同行之间用换行符来替代
#     # print(content)
#
#     # # 换行读取
#     # line = file.readline()# 因为本来就是以行的形式存储的，因此原本数据中的换行符会导致最后的结果多出一个空行
#     # while line:
#     #     print(line)
#     #     line = file.readline()
#
#     # # 全部行读取
#     # lines = file.readlines()  # 因为本来就是以行的形式存储的，因此原本数据中的换行符会导致最后的结果多出一个空行,但我用strip将换行符删除了
#     # for line in lines:
#     #     print(line.split(" ")[1].rstrip('\n'))
#
#     # # 文件本身就是一个迭代器
#     # for line in file:  # 效果和行读取一样的
#     #     print(line)
#
#     # # 添加数据
#     # # file.write("\n5 6")
#     # write = ["\n7 8 ", "\n9 10 ", "\n11 12 "]  # 这儿的换行符是必须的，否则的话，会连在一起
#     # file.writelines(write)
#
#     # # 指针
#     # content = file.read(4)  # 换行符占用一个字符
#     # print(content)
#     # file.seek(1)
#     # content = file.read(4)
#     # print(content)

# # os 读取csv
# with open("example.csv", "r+", encoding="utf-8") as file:
#     # content = file.read()
#     # print(content)
#     # lines = file.readlines()
#     # for line in lines:
#     #     print(line.rstrip("\n"))
#     # （1）seek(offset[, whence])：
#     # （2）offset - -偏移量，可以是负值，代表从后向前移动；
#     # （3）whence - -偏移相对位置，分别有：os.SEEK_SET（相对文件起始位置，也可用“0”表示）；os.SEEK_CUR（相对文件当前位置，也可用“1”表示）；os.SEEK_END（相对文件结尾位置，也可用“2”表示）。
#
#     file.seek(0, 2)
#     file.write('\n1,2')

# # csv库读取csv
# with open("example.csv", "r+", encoding="utf-8") as file:
#     content = csv.reader(file)  # 直接读content是读不出来的
#     for line in content:
#         print(line)


# # # 处理结构化数据文件，例如 CSV、Excel、JSON 等，可以使用 pandas 库。
content = pd.read_csv("example.csv", dtype={'语文': "str", "数学": "float"}, encoding="utf-8")
# print(content['语文'])
# print(content.loc[1:2, '语文'])  # loc，在知道列名字的情况下，df.loc[index,column] 选取指定行，列的数据
# print(content.iloc[0, 0])  # loc，在知道列名字的情况下，df.loc[index,column] 选取指定行，列的数据

# # 处理数值数据文件，例如文本文件中的数值数据，可以使用 numpy 库。
# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(a[1, 1])
# array_txt = np.loadtxt("example.txt", dtype=int)
# print(array_txt[0, 1])
# scores = np.random.randint(0, 100, size=(50, 2))
# np.savetxt("example.csv", scores, delimiter=",", header="语文,数学", encoding='utf-8', comments='')  # comments注释默认为#号，这儿需要给去除
# # csv用半角逗号（’,’）作为字段值的分隔符。
# scores = np.loadtxt("example.csv",delimiter=",",dtype=float,skiprows=1,encoding='utf-8')#在读取的时候就可以转换格式
# scores = np.loadtxt("example.csv",delimiter=",",dtype=None,encoding='utf-8')#在读取的时候就可以转换格式
# print(type(scores[1,1]))
# scores = np.loadtxt("example.txt",dtype=str)
# print(scores)
# a = np.arange(1,7).reshape(2,3)

# file = open("example.txt", "r+")
# print(file.read())
# file.close()

# # 字典按照value和key排列
# d = {'a': 1, 'b': 4, 'c': 2}
#
# print(sorted(d.items(), key=lambda x: x[1], reverse=True))
# print(sorted(d.items(), key=lambda x: x[0], reverse=True))  # 匿名函数

# 位运算：将对象转换为对应的补码，然后进行运算
# &	按位运算符，参与运算的两个值，如果相应位都为1，则该位的结果为1，否则为0
# ^	按位异或运算符，当两个对应的二进位相异时，结果为1
# ~	按位取反运算符，对数据的每个二进制位取反，即把1变为0，把0变为1
# |	按位或运算，只要对应两个二进制位有一个为1时，结果就为1
# <<	左移动运算符：运算数的各二进制位全部左移若干位，由 << 右边的数字指定了移动的位数，高位丢弃，低位补0
# >>	右移动运算符：把>>左边的运算数的各二进制位全部右移若干位，>> 右边的数字指定了移动的位数
# >>> 3 & 5
# 1
# 0000 0011  # 3的补码
# 0000 0101  # 5的补码
# 0000 0001  # 根据按位与的规则，得出补码结果

# 匿名函数
func = lambda x, y: x * y
print(func(1, 2))
print(list(map(func, [1, 2], [3, 4])))  # map(function, iterable, ...),python3中返回的是一个迭代器
print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])))  # filter(function, iterable)
print(reduce(lambda x, y: x * y, [1, 2, 3, 4, 5]))  # educe() 函数会对参数序列中元素进行累积。
# 函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。
print('[1,2,3,4,4]列表的众数为:', statistics.mode([1, 2, 3, 4, 4]))

time_2 = time.time()
print("花费时间", time_2 - time_1)
