
'''
把爬进来的csv文件的一条条文本进行情感分析
得出的值放入excle文本中

'''
import snownlp
import pandas as pd
import numpy as np
import re
import itertools
import matplotlib.pyplot as plt
import jieba
import random

content=open(r"D:\数据\python 代码\能用的小东西\练习类\comment1.csv","r",encoding="gbk").read()
# word=snownlp.SnowNLP(content)
txtlist=jieba.lcut(content)
random.shuffle(txtlist)
txtlist=set(txtlist)
# print(txtlist)
posttivelist=[]
negativelist=[]

print("开始进行情感分析")
for each in txtlist:
    each_word=snownlp.SnowNLP(each)
    feeling=each_word.sentiments
    if feeling > 0.96:
        posttivelist.append(each)
    elif feeling < 0.1:
        negativelist.append(each)
    else:
        pass

# 载入情感分析后的数据

from gensim import corpora, models
# 建立词典
pos_dict = corpora.Dictionary([[i] for i in posttivelist])  # 正面
neg_dict = corpora.Dictionary([[i] for i in negativelist])  # 负面

# print(pos_dict)
# 建立语料库
pos_corpus = [pos_dict.doc2bow(j) for j in [[i] for i in posttivelist]]  # 正面
neg_corpus = [neg_dict.doc2bow(j) for j in [[i] for i in negativelist]]   # 负面
print(pos_corpus)
# 构造主题数寻优函数
def cos(vector1, vector2):  # 余弦相似度函数
    dot_product = 0.0;  
    normA = 0.0;  
    normB = 0.0;  
    for a,b in zip(vector1, vector2): 
        dot_product += a*b  
        normA += a**2  
        normB += b**2  
    if normA == 0.0 or normB==0.0:  
        return(None)  
    else:  
        return(dot_product / ((normA*normB)**0.5))   

# 主题数寻优
def lda_k(x_corpus, x_dict):  
    
    # 初始化平均余弦相似度
    mean_similarity = []
    mean_similarity.append(1)
    
    # 循环生成主题并计算主题间相似度
    for i in np.arange(2,11):
        lda = models.LdaModel(x_corpus, num_topics=i, id2word=x_dict)  # LDA模型训练
        for j in np.arange(i):
            term = lda.show_topics(num_words=50)
            
        # 提取各主题词
        top_word = []
        for k in np.arange(i):
            top_word.append([''.join(re.findall('"(.*)"',i)) \
                           for i in term[k][1].split('+')])  # 列出所有词
           
        # 构造词频向量
        word = sum(top_word,[])  # 列出所有的词   
        unique_word = set(word)  # 去除重复的词
        
        # 构造主题词列表，行表示主题号，列表示各主题词
        mat = []
        for j in np.arange(i):
            top_w = top_word[j]
            mat.append(tuple([top_w.count(k) for k in unique_word]))  
            
        p = list(itertools.permutations(list(np.arange(i)),2))
        l = len(p)
        top_similarity = [0]
        for w in np.arange(l):
            vector1 = mat[p[w][0]]
            vector2 = mat[p[w][1]]
            top_similarity.append(cos(vector1, vector2))
            
        # 计算平均余弦相似度
        mean_similarity.append(sum(top_similarity)/l)
    return(mean_similarity)
            
# 计算主题平均余弦相似度
pos_k = lda_k(pos_corpus, pos_dict)
neg_k = lda_k(neg_corpus, neg_dict)        

# 绘制主题平均余弦相似度图形
from matplotlib.font_manager import FontProperties  
font = FontProperties(size=14)
#解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False  
fig = plt.figure(figsize=(10,8))
ax1 = fig.add_subplot(211)
ax1.plot(pos_k)
ax1.set_xlabel('正面评论LDA主题数寻优', fontproperties=font)

ax2 = fig.add_subplot(212)
ax2.plot(neg_k)
ax2.set_xlabel('负面评论LDA主题数寻优', fontproperties=font)

# LDA主题分析
pos_lda = models.LdaModel(pos_corpus, num_topics=3, id2word=pos_dict)  
neg_lda = models.LdaModel(neg_corpus, num_topics=3, id2word=neg_dict)  
a=pos_lda.print_topics(num_words=10)
b=neg_lda.print_topics(num_words=10)
print(a)
# plt.show()









