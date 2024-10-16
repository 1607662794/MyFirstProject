# 该文档用于我练手的一些代码，包括字典排序，文件读取等。
# coding:utf-8
import collections
import copy

import csv
import math
import os
import statistics
import time
from functools import reduce
import heapq

import numpy
import numpy as np
import pandas as pd
import torch
from tqdm import tqdm
from collections import Counter
from collections import deque
import queue
import json
from itertools import zip_longest

# 时间函数
time_1 = time.time()

# # 目录地址
# print(os.path.isdir(os.getcwd()))
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

# 进度函数
# for i in tqdm(os.listdir()):
#     if i.split(".")[-1] == 'py':
#         print(i)
# print("\t")

# # 数学运算
# print("6/5向上取整；", math.ceil(6/5))
# print("6/5向下取整；", math.floor(6/5))
# print('5的根号等于{}'.format(math.sqrt(5)))
# print("6/5四舍五入；", round(6/5))
# print("6/5四舍五入，并保留位数；", round(5 / 3, 6))
# print("[1,2,3]的平均数为{}".format(numpy.average([1,2,3])))#[1,2,3]的平均数为2.0,numpy.float64
# print("[1,2,3]的平均数为{}".format(statistics.mean([1,2,3])))#[1,2,3]的平均数为2

# # 常见操作
# print("字符串分割，括号内的形参可以指定个数","abc".split())
# print("单词分割为字母",list('abc'))
# print("字母合并为单词",''.join(['a','b','c']))
# print("移除字符串头头尾的指定字符，默认为空格，左删除为lstrip(),右删除为rstrip()","  Hello,World  ".strip())
# print("计数{}".format("abc".count('a')))
# print("'abc是否是以a开头的".format('abc'.startswith('a')))
# print("'abc是否是以c开头的".format('abc'.endswith('c')))


# # 本机配置
# print("输出cpu的颗数", os.cpu_count())

# 无穷大
# print(math.inf)
# print(-math.inf)

# # 字符 →→ ASCII码
# print("1~9的ASCII分布：{}~{}".format(ord('1'), ord('9')))
# print("a~z的ASCII分布：{}~{}".format(ord('a'), ord('z')))
# print("A~Z的ASCII分布：{}~{}".format(ord('A'), ord('Z')))
#
# # ASCII码 →→ 字符
# print(chr(49))

# json命令
# python对象转换为json对象
# data = {'name': 'John', 'age': 30, 'city': 'New York'}
# json_string = json.dumps(data)
# print(json_string)
# json_string = json.dumps(data,indent=4)
# print(json_string)

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


# # 处理结构化数据文件，例如 CSV、Excel、JSON 等，可以使用 pandas 库。
# content = pd.read_csv("example.csv",encoding="utf-8",dtype={'语文': "float", "数学": "float"})
# content = pd.read_csv("example.csv", dtype={'语文': "str", "数学": "float"}, encoding="utf-8")
# print(content['语文'])
# print(content.loc[1:2, '语文'])  # loc，在知道列名字的情况下，df.loc[index,column] 选取指定行，列的数据
# print(content.iloc[0, 0])  # loc，在不知道列名字的情况下，df.loc[index,column] 选取指定行，列的数据


# # 处理数值数据文件，例如文本文件中的数值数据，可以使用 numpy 库。
# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(a[1, 1])
# array_txt = np.loadtxt("example.txt", dtype=int)
# print(array_txt[0, 1])
# scores = np.random.randint(0, 100, size=(50, 2))
# np.savetxt("example.csv", scores, delimiter=",", header="语文,数学", encoding='utf-8', comments='')  # comments注释默认为#号，这儿需要给去除
# # csv用半角逗号（’,’）作为字段值的分隔符。
# scores = np.loadtxt("example.csv",delimiter=",",dtype=float,skiprows=1,encoding='utf-8')#在读取的时候就可以转换格式
# print(type(scores[1,1]))
# scores = np.loadtxt("example.txt",dtype=str)
# print(scores)
# a = np.arange(1,7).reshape(2,3)

data = np.genfromtxt(r"E:\Code\Hysteretic curve processing\sampling_data\RS3_time_appended.csv", delimiter=',',
                     skip_header=1,
                     dtype=[('image_names', 'U50'), ('u [mm]', float), ('Fh [kN]', float), ('times [s]', int)])

# file = open("example.txt", "r+")
# print(file.read())
# file.close()

# 函数any
# print(any([1, 2, 3, 0]))  # 返回True


# # 列表
# print([1, 2, 3, 4])
# print([1, 2, 3, 4][-1:2:-1])#返回[4]切片，负数代表从右向左切
# a = [1, 2, 3, 4]
# a.remove(2)
# print(a)  # 删除值
# del a[1]
# print(a)  # 删除索引
# a.insert(1, 0)  # 在1处插入0
# print(a)
# a.append(3)
# a.extend(a)#逐个添加元素
# print(a)
# print(a.index(4, -2, -1))  # 后边可以输入查找范围
# print(sorted('bca'))#排序之后为一个列表
# 创建一个多元数组
# a = [0] * 2
# # 创建一个不同维度大小的数组，以杨辉三角为例
# dp = [[1] * (i + 1) for i in range(5)]
# print(dp)
# # 列表相加的结果
# a = [1, 2]
# b = [3, 4]
# print(a + b)#这种方式倒是和extend的功能挺像的。
#
# for i in range(2, 1):  # 如果这两个超参不合规律的话，并不会报错，只是不会执行。
#     print('倒序不能输出')

# # range的循环次数在第一次计算结束后就确定了，并不会因为列表的变化而变化
# a = [1,2,3]
# for i in range(len(a)):
#     a.append(1)
#     print("循环次数{}".format(i))


# 集合,可以看做是只有关键字的字典，无重复值，另外，对集合的查询或者修改要比列表快很多，这也是为什么很多题目可以用集合做
# 不超时，而用列表做时，会超时
# a = [1, 2, 3, 2]
# a = set(a)
# print(a)
# a = (1, 2, 3, 2)
# a = set(a)
# print(a)
# a.add(5)
# a.remove(1)  # 删除元素
# print("集合{{1,2,3}}添加元素5后变成了{}".format(a))


# 元组
# 元组是可读的，但是不能被修改
# a = (1, 2, 3)#不使用set的话，是元组，而不是集合。
# print(a)
# print(a[1])


# # 整除与取余
# print("整除4//3得{}".format(4//3))
# print("取余4%3得{}".format(4 % 3))
# # 列表多级排序
# x_1 = [1,2,3,4]
# x_2 = [1,1,2,2]
# x_3 = [4,3,2,1]
# score = []
# for i in range(len(x_1)):  # 合并成元组列表
#     score.append((x_1[i],x_2[i],x_3[i]))
# score = sorted(score, key = lambda x : (x[1],x[2]))  # key:一个只有一个参数的函数，这个函数会被用在序列里的每一个元素上，所产生的结果将是排序算法依赖的对比关键字。
# print(score)

# # 字典按照value和key排列
# d = {'a': 1, 'b': 4, 'c': 2}
#
# print(sorted(d.items(), key=lambda x: x[1], reverse=True)) # [('b', 4), ('c', 2), ('a', 1)]
# print(sorted(d.items(), key=lambda x: x[0], reverse=True))  # 匿名函数
# d ={[1,2,3]:1} #因为哈希的关键字是不能变的，因此这儿采用列表的话，就会出问题。

# # defaultdict方法:正常定义字典的情况下，如果关键字不在的话，将导致报错。通过collections.defaultdict(int)，将为字典设置一个默认的值，如0，将取消异常
# your_dict = {"a",1}
# print(your_dict)
# my_dict = collections.defaultdict(int)
# my_dict['a']
# print(my_dict)


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
# 0000 0001  # 根据按位与的规则，得出补码结果，最后的补码结果需要先看符号位，决定是否先减1，变为反码，然后再变为原码
# 任何数和0做异或运算，结果是自身
# print("0与任何数异或操作结果仍为那个数：{}".format(0 ^ 2))

# 补码显示
def int_to_16bit_binary(n):
    # 定义16比特的范围
    MIN_VALUE = -32768
    MAX_VALUE = 32767

    # 限制输入范围
    if n < MIN_VALUE:
        n = MIN_VALUE
    elif n > MAX_VALUE:
        n = MAX_VALUE

    # 转换为补码
    if n < 0:
        n = (1 << 16) + n  # 负数的补码表示

    # 转换为二进制字符串，填充至16位
    binary_representation = format(n, '016b')

    return binary_representation


# # 匿名函数
# func = lambda x, y: x * y
# print(func(1, 2))
# print(list(map(func, [1, 2], [3, 4])))  # map(function, iterable, ...),python3中返回的是一个迭代器，返回[3,8]
# print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])))  # filter(function, iterable)
# print(reduce(lambda x, y: x * y, [1, 2, 3, 4, 5]))  # reduce() 函数会对参数序列中元素进行累积。
# # 函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。
# print('[1,2,3,4,4]列表的众数为:', statistics.mode([1, 2, 3, 4, 4]))

# 进制转换
# 转换为2进制→bin，转换为8进制→oct，转换为10进制→int，转换为16进制→hex，所有的转换都需要经过10进制。
# n = int(input())
# print("2进制转换为8进制{}".format(oct(int('010', 2))), end=' ')

# # 输出格式化
# print("输出保留两位小数{:.2f}".format(1.22225))
# print("输出保留两位小数(带符号）{:+.2f}".format(1.22225))
# print("输出保留两位小数(带符号）{:-.2f}".format(1.22225))
# print("指数计法{:.2e}".format(1.22225))
# print("百分比{:.2%}".format(1.22225))
# print("左边填充0,注意只有整数可以{:0>8d}".format(1))
# print("左边填充x,注意只有整数可以{:x>8d}".format(1))
# print("20的八进制表示{:o}".format(20))
# print("20的16进制表示{:x}".format(20))
# print()

# ACM模式
# while True:
#     # line = input().strip().split(" ")
#     # a,b = int(line[1]),int(line[0])
#     # print(a+b)
#
#     # line = input().lower()
#     # print(line)
#
#     try:
#         # number = int(input())
#         # tree_list = list(map(int, input().strip().split(" ")))
#         # my_list = []
#         # for i in range(number):
#         #     my_list.append(int(input()))
#         # my_list = set(my_list)
#         # my_list = list(my_list)
#         # print(my_list)
#
#         # l = input()
#         # for i in range(0, len(l), 8):
#         #     print("{:0<8s}".format(l[i:i + 8]))#右边用0来填充
#
#     except:
#         break

# 翻转,reverse翻转后的对象不是列表，是一个可迭代对象，在这儿需要转换一下。
# a = ['a', 'b', 'c']
# print("a被翻转{}".format(list(reversed(a))))
# print("a并未被翻转{}".format(a))
# print("a被翻转{},返回值是一个None".format(a.reverse()))
# print("a被翻转{}".format(a))
# a[1:] = list(reversed(a[1:]))
# print("a的后两个元素进行切片颠倒，然后子列表进行赋值，也是可以的，结果为{}".format(a))

# # 基础运算
# print("对数函数{}".format(math.log(100, 10)))  # 2.0
# print(str([1, 2, 3]))
# print(list(map(str, [1, 2, 3])))
# print("python中是可以进行字符串比较大小的。".format('123' < '23'))

# 技巧
# 字符串从左边开始向右比较
a = ['123', '23', '124']
a.sort(key=lambda x: (x * 10)[:10])
print(a)

# 计算约数
# def count_divisors_up_to_r(r):
#     divisor_counts = [0] * (r + 1)  # 创建一个长度为 r+1 的列表来存储每个数的约数数量
#
#     for i in range(1, r + 1):
#         for j in range(i, r + 1, i):
#             divisor_counts[j] += 1  # 增加每个 i 的倍数的约数数量
#
#     return divisor_counts[1:]  # 返回从 1 到 r 的约数数量列表

# for 循环
# 注意，循环内的变量也是局部变量的一种。
# for i in range(2):
#     print("当前循环下的i值为{}".format(i))
# print("循环结束后的i值为{}".format(i))  # 为1

# # 列表计数
# nums = [-1, -1, 1, 2, 3]  # 排序如果直接按照.count来计数的话会出现负数排序不正确的情况
# counter = Counter(nums)#并且是值默认为零。主要包不包含关系可以直接通过比较大小得到，而collections.defaultdict(int)无法进行比较。
# print(counter)
# top_k = sorted(counter.keys(), key=lambda x: counter[x], reverse=True)[:2]
# print(top_k)

# # 双向队列
# str = 'abc'
# list_1 = [1, 2, 3]
# queue_1 = deque(str)
# queue_2 = deque(list_1)
# # 右端加入
# queue_1.append(4)  # deque(['a', 'b', 'c', 4, 'k'])
# print(queue_1)
# queue_1.append('k')  # deque([1, 2, 3])
# 左端加入
# queue_1.appendleft(4)#deque(['k', 4, 'a', 'b', 'c'])
# queue_1.appendleft('k')#deque([1, 2, 3])
# 向右端逐个添加可迭代对象
# ex = [1,'h',2]
# queue_1.extend((ex))#deque(['a', 'b', 'c', 1, 'h', 2])
# queue_2.extend((ex))#deque([1, 2, 3, 1, 'h', 2])
# 向左端逐个添加可迭代对象
# ex = [1,'h',2]
# queue_1.extendleft((ex))#deque([2, 'h', 1, 'a', 'b', 'c'])
# queue_2.extendleft((ex))#deque([2, 'h', 1, 1, 2, 3])
# 移除队列中的一个元素
# print(queue_1.pop())#c
# print(queue_1)#deque(['a', 'b'])
# 移除队列中左边的一个元素
# print(queue_1.popleft())#a
# print(queue_1)#deque(['b', 'c'])
# 在指定位置插入一个元素
# queue_1.insert(1,'vf')#deque(['a', 'vf', 'b', 'c'])
# print(queue_1)
# print(queue_2)


# if not 0:
#     print("0在Python中被判定为False")

# # 队列
# q = queue.Queue()
# q.put(1)
# q.put(3)
# print(q.get())  # 输出：1
# print(q.get())  # 输出：2
# print(q.get())  # 输出：3

# # 栈
# q = queue.LifoQueue()
# q.put(1)
# q.put(2)
# q.put(3)
# print(q.get())  # 输出：3
# print(q.get())  # 输出：2
# print(q.get())  # 输出：1
# if q.empty:
#     print('q为空')
# print('q的尺寸为{}'.format(q.qsize()))

# # 堆
# min_heap = []
# heapq.heappush(min_heap, 1)
# heapq.heappush(min_heap, 2)
# heapq.heappush(min_heap, 3)
# heapq.heappop(min_heap)  # 将堆heap中最小的元素弹出并返回，堆发生改变。
# print(min_heap)  # 输出小根堆，默认的就是构建小根堆
# max_heap = []
# for i in range(3):
#     heapq.heappush(max_heap, -i)
# a = [1, 2, 3]
# heapq.heapify(a)  # 将列表x转换成堆。
# heapq.heapreplace(min_heap, 2)  # 弹出堆heap中最小的元素，并将元素item加入堆中。
# 如果比较的是对象，如链表，那么在开头加一句话以修改魔术方法即可
# 如果保存的是对象，会触发对象的比较大小的魔术方法，因此只需要重定义一下类似于 __lt__ 这种方法即可。
# ListNode.__lt__ = lambda a, b: a.val < b.val
# # 构建索引与值的字典
# index = {element: i for i, element in enumerate(['a', 'b', 'c', 'd'])}

# 二元组在小根堆中的存储顺序
# example = [(1, 2), (3, 4), (2, 0)]
# heapq.heapify(example)  # 注意，转换类型后不要对其进行赋值
# print(example)  # 输出为[(1, 2), (3, 4), (2, 0)]，也就是说此时的顺序还没有发生改变。调用heapq.heapify()函数时，它会将列表转换成一个堆数据结构，但是这并不意味着列表会变成一个排序好的列表。但是可以确定的是，第一个元素一定是最小的
# print(heapq.heappop(example))#弹出的时候是正常的
# print(example)#弹出一个值后，后边的值顺序就会发生变化。
# print(heapq.heappop(example))#弹出的时候是正常的
# print(example[0])
# example = [2, 1, 3]
# heapq.heapify(example)
# print(example)  # 此时的输出是排序后的结果


# 在Python中使用heapq模块处理二元组（或任何元组）时，小根堆默认会根据元组的第一个元素进行排序。如果第一个元素相同，则会比较第二个元素
# # 创建一个空的堆,
# heap = []
# # 元组包含(value, index)
# data = [(3, 2), (1, 5), (2, 1), (3, 1)]
# # 将数据压入堆中
# for item in data:
#     heapq.heappush(heap, item)
# # 从堆中弹出最小的元素
# while heap:
#     print(heapq.heappop(heap))

# # 字典操作
# dict_pri = {'a': 1, 'b': 2, 'c': 3}
# for i,w in enumerate(dict_pri):
#     print('{}:{}'.format(i,w))#字典的遍历将会丢失其值。
# del dict_pri['a']
# print(dict_pri.get('a'))  # 返回指定键的值，如果值不在字典中返回default值，默认是None
# if None:  # None值并不会被判定为False
#     print('Hello')
# print(dict_pri.items())  # 以列表返回可遍历的(键, 值) 元组数组
# print(dict_pri.keys())  # 以列表返回一个字典所有的键
# print(dict_pri.values())  # 以列表返回字典中的所有值

# 对于类型值的判断
a = 1
print(type(a) == int)  # True, 在进行类别判断的时候，不需要加入引号，
print(type(a) == 'int')  # False, 在进行类别判断的时候，不需要加入引号，

# 打包函数，按照两个序列的最大长度来。
x = [1, 1, 2]
y = [1, 2]
for a, b in zip_longest(x, y, fillvalue=0):  # 注意在itertools库中导入该工具。
    print(a, b)

# 打包函数，默认是按照两个序列的较短长度来的。
for a, b in zip(x, y):
    print(a, b)

# strip()函数，注意其并非原地操作，若要改变值的话，需要额外赋值。
a = ' abs c '
print(a.strip())
# strip函数同样可以对特定字符进行删除
a = 'avs'
print(a.strip('s'))

# 局部变量
a = 1


def func(x):
    x = 2


func(a)
print(a)  # 输出1

b = [1]  # 列表是可变对象，因此，在接下来的传递过程中，传递给函数形参的是对列表对象的引用，因此在函数内部对列表对象的操作会同时影响到列表本身。


def func(x):
    x.append(2)


func(b)
print(b)  # 输出[1,2]

# if 0:  # 条件判断0不会被执行
#     print('Hello world')

# 二维列表的复制
matrix = [[1, 2], [3, 4]]
copy_matrix = [[matrix[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]

# 拷贝
a = [1, 2]
b = copy.copy(a)
c = copy.deepcopy(a)

# split函数
a = 'da ad  das'
print(a.split())  # 如果不指定的话，会以默认符号进行分割。

# 正则表达
# https://blog.csdn.net/guo_qingxia/article/details/113979135

# # 张量运算
# a = torch.tensor([1, 2, 3])
# print(a.unsqueeze(-1))
# b = torch.arange(0, 5).unsqueeze(dim=1)
# print(b)

# view,变化张量形状，但是元素数量不变。

# squeeze用于移除张量中所有大小为1的维度，当时我在训练自己的神经网络模型的时候就没有用到该函数。

# cat和concat用于沿着某一维度将两个张量拼接起来

# stack 用于在一个新的维度将两个张量拼接起来。
#
# # transpose交换维度
# print(b.transpose(0,1))
#
# # 指数运算时，会将张量列表中的每一个元素都进行处理。
# print(math.log(10))
# print(torch.exp(torch.arange(5))*2)
# print(3 // 2)
#
# # 上三角矩阵
# shape = [4,10,10]
# subsequence_mask = np.triu(np.ones(shape),k=1)  # 直接生成4个10*10的上三角矩阵。
# subsequence_mask = torch.from_numpy(subsequence_mask).byte()
# print(subsequence_mask)

time_2 = time.time()
print("花费时间", time_2 - time_1)
