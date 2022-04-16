
'''
评论分词后主题分析


'''
import snownlp
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import jieba
import random
from gensim import corpora, models
from collections import Counter

content=open(r"D:\数据\python 代码\能用的小东西\练习类\comment1.csv","r",encoding="gbk").read()
# word=snownlp.SnowNLP(content)

# print(txtlist)
punctuation = '!,;:?"\'\n，'

def removePunctuation(text):

    text = re.sub(r'[{}]+'.format(punctuation),'',text)

    return text.strip().lower()
  
txtlist1=removePunctuation(content)
txtlist1=jieba.lcut(txtlist1)
txtlist=[]
# print(txtlist)
for word in txtlist1:
    if len(word)>1:      #一个字的词删了
        txtlist.append(word) 
random.shuffle(txtlist)

# txtlist=set(txtlist)
# wd=Counter(txtlist)


# 载入情感分析后的数据

# txtlist=wd.most_common(300)
dff=pd.DataFrame(txtlist)
print(dff[0])
       
pos_dict = corpora.Dictionary([[i] for i in dff[0]])  # 正面
pos_corpus = [pos_dict.doc2bow(j) for j in [[i] for i in dff[0]]] 
# print(pos_dict)
# print("hao")

# LDA主题分析
pos_lda = models.LdaModel(pos_corpus, num_topics=20,id2word=pos_dict)  


a=pos_lda.print_topics(num_words=20)
# print(a)
df=pd.DataFrame(a)
df.to_csv("D:\数据\python 代码\能用的小东西\练习类\data1.csv",encoding='gbk')
# print(a)










