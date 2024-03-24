import re
import math

# 举例
stopword = "a,an,the"

# 将停用词表转换为集合
stopwords = set(stopword.split(","))

# 读取文件
with open("article.txt", "r") as f:
    sentences = f.readlines()

# 计算词频
word_freq = {}
for sentence in sentences:
    words = re.split("[ ,.!]", sentence.strip().lower())  # 全部小写，因为大小写对应的是同一个词
    for word in words:
        if word not in stopwords:
            word_freq[word] = word_freq.get(word, 0) + 1  # 如果没有，那就代表0个

# 计算文档总数
doc_num = len(sentences)

# 计算逆文档频率，如果仅仅计算idf，那么到这一步就结束了。
word_idf = {}
for word, freq in word_freq.items():
    doc_count = 0
    for sentence in sentences:
        if word in sentence:
            doc_count += 1
    word_idf[word] = math.log(doc_num / (doc_count + 1))

# 计算 if-idf 值
word_tfidf = {}
for word, freq in word_freq.items():
    word_tfidf[word] = freq * word_idf[word]

# 排序并输出前 10 个非停用词的 idf 值
sorted_words = sorted(word_tfidf.items(), key=lambda x: x[1], reverse=True)
for word, tfidf in sorted_words[:10]:
    if word not in stopwords:
        print(word, tfidf)
