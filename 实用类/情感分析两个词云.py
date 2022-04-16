'''
2022.2.26   23.37
整词云
'''

from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt
import snownlp
import jieba
import imageio 
import random

image=imageio.imread('picture/购物车3.jpg') 
stop={'用户','点赞数','评论','发表时间','第','页','的','是','你','了','不'}
content=open(r"能用的小东西/实用类/weibo.txt","r",encoding="utf-8").read()
# word=snownlp.SnowNLP(content)
txtlist=jieba.lcut(content)
random.shuffle(txtlist)

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

w1=WordCloud(background_color='white',width=1000,height=700,mask=image,
font_path='msyh.ttc',stopwords=stop,scale=15)

w2=WordCloud(background_color='white',width=1000,height=700,mask=image,
font_path='msyh.ttc',stopwords=stop,scale=15)

posttivelist=" ".join(posttivelist)
negativelist=" ".join(negativelist)

w1.generate(posttivelist)
w2.generate(negativelist)

w1.to_file("能用的小东西/实用类/情感分析postive.png")
w2.to_file("能用的小东西/实用类/情感分析negative.png")
print('ok了')



