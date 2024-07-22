# 手撕Attention
import math

import numpy as np
import torch
from torch import nn
import torch.utils.data as Data

# class ScaleDotProductAttention(nn.Module):
#     "Scaled Dot-Product Attention"
#
#     def __init__(self, scale):
#         super().__init__()
#
#         self.scale = scale
#         self.softmax = nn.Softmax(dim=2)
#
#     def forward(self, q, k, v, mask):  # 此处的掩码矩阵中值均为Boolen
#         u = torch.bmm(q, k.transpose(1, 2))
#         u = u / self.scale
#
#         if mask is not None:
#             u.masked_fill(mask, -np.inf)
#
#         atten = self.softmax(u)  # 计算注意力
#         output = torch.bmm(atten, v)  # 将计算出来的注意力与value值进行相乘。
#
#         return atten, output

# # nn.Softmax
# func = nn.Softmax(dim=0)  # 表示对输入张量的第几维进行归一化,[0][0][0]与[1][0][0]和为1.
# objecct = torch.randn(2, 3, 2)
# print(func(objecct))

# # nn.bmm对两个3维张量进行乘积，第一维往往指的是batch_size
# object_1 = torch.randn(4,2,3)
# object_2 = torch.randn(4,3,2)
# print(torch.bmm(object_1,object_2).size())


# Transformer实例

# 设别选项
device = 'cuda'

# 训练批次
epoch = 100

# S表示输入编码的开始
# E表示输出编码的开始
# P代表如果当前批次尺寸小于时间步的话，需要填充的横线序列

# 训练语料
sentences = [
    ['我 有 一 个 好 朋 友 P', 'S I have a good friend .', 'I have a good friend . E'],
    ['我 有 零 个 女 朋 友 P', 'S I have zero gril friend .', 'I have zero gril friend . E'],
    ['我 有 一 个 男 朋 友 P', 'S I have a boy friend .', 'I have a boy friend . E']
]

# 测试集
# 输入：我有一个女朋友
# 输出：i have o gril friend

# 中文和英文的单词要分开建立词库
src_vocab = {'P': 0, '我': 1, '有': 2, '一': 3, '个': 4, '好': 5, '朋': 6, '友': 7, '零': 8, '女': 9, '男': 10}
src_index2word = {i: j for i, j in enumerate(src_vocab)}
src_vocab_size = len(src_vocab)

tgt_vocab = {'P': 0, 'I': 1, 'have': 2, 'a': 3, 'good': 4, 'friend': 5, 'zero': 6, 'gril': 7, 'boy': 8, 'S': 9, 'E': 10,
             '.': 11}
tgt_index2word = {i: j for i, j in enumerate(tgt_vocab)}
tgt_vocab_size = len(tgt_vocab)

src_len = 8  # 源句子的长度
tgt_len = 7  # 输出解码的最长序列

# Transformer的必要参数
d_model = 512
d_ff = 2048
d_k = d_v = 64
n_layers = 6
n_heads = 8


def make_data(sentences):
    '''将单词序列转换为数字序列'''
    enc_inputs, dec_inputs, dec_outputs = [], [], []
    for i in range(len(sentences)):
        enc_input = [[src_vocab[i] for i in sentences[0].split()]]
        dec_input = [[src_vocab[i] for i in sentences[1].split()]]
        dec_output = [[src_vocab[i] for i in sentences[2].split()]]

        enc_inputs.extend(enc_input)
        dec_inputs.extend((dec_input))
        dec_outputs.extend((dec_output))  # 如果前面用一重列表，然后这儿使用append效果是一样的。

    return torch.LongTensor(enc_inputs), torch.LongTensor(dec_inputs), torch.LongTensor(dec_outputs)  # 其内元素为整型的张量


enc_inputs, dec_inputs, dec_outputs = make_data(sentences)

class MyDataSet(Data.Dataset):
    '''自定义dataloader'''
    def __init__(self,enc_inputs,dec_inputs,dec_outputs):
        super(MyDataSet,self).__init__()
        self.enc_inputs = enc_inputs
        self.dec_inputs = dec_inputs
        self.dec_output = dec_outputs

    def __len__(self):
        return self.enc_inputs.shape[0]

    def __getitem__(self, idx):
        return self.enc_inputs[idx], self.dec_inputs[idx],self.dec_output[idx]

loader = Data.DataLoader(MyDataSet(enc_inputs,dec_inputs,dec_outputs), batch_size=2, shuffle=True)

#定义模型
class PositionalEncoding(nn.Module):
    def __init__(self,d_model,dropout=0.1,max_length=5000):
        super(PositionalEncoding,self).__init__()
        self.dropout = nn.Dropout(p=dropout)

        pe = torch.zeros(max_length,d_model)
        position = torch.arange(0,max_length,dtype=torch.float).unsqueeze(1)#unsqueeze的作用是给n*1的张量进行降维，降维为1*n，但我不太理解，为什么在这儿需要降维
        # 但有一点挺奇怪的，就是原本是一个一维的张量，我经过压缩之后反而成了一个多维的张量，其实是对的，因为后边要与一个1*d_model的矩阵相乘，乘积后的结果为一个max_lenght*(d_model/2)的矩阵
        div_term = torch.exp(torch.arrage(0,d_model,2).float()*(-math.log(1000.0)/d_model))
        pe[:,0::2] = torch.sin(position*div_term)
        pe[:,1::2] = torch.cos(position*div_term)
        self.register_buffer('pe',pe)#其实就是self.pe = pe

    def __forward(self,x):
        x = x + self.pe[:x.size(0),:]#看每个样本的长度，只是在存在的部分添加位置编码，其余部分也就没必要的，但是语义仍然是相当于有d_model个
        return x

def get_attn_pad_mask(seq_q,seq_k):


