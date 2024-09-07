# https://blog.csdn.net/qq_43858783/article/details/134543721
# 相当于在原来的bert输出处，添加了下游任务网络，然后冻结原bert网络部分，进行新的训练。
import os
from transformers import BertTokenizer, BertModel, AdamW

os.environ['CURL_CA_BUNDLE'] = ''
os.environ['REQUESTS_CA_BUNDLE'] = ''

# 定义数据集
# 加载tokenizer
token = BertTokenizer.from_pretrained('bert-base-chinese')
print('token', token)
