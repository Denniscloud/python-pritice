'''
2022.2.26   23.37
整词云
'''

#    提取图片颜色让词云的颜色随图片颜色变化

from wordcloud import WordCloud,ImageColorGenerator
import matplotlib.pyplot as plt
import jieba
import imageio 
import random
from collections import Counter
import pandas as pd


image=imageio.imread('picture/购物女1.jpg')

image_color=ImageColorGenerator(image)   #提取颜色
f=open(r"D:\数据\python 代码\能用的小东西\练习类\data.txt","r",encoding="gbk")
content=f.read()
content1=open(r"能用的小东西/实用类/商场买什么.txt","r",encoding="utf-8").read()
stop={'项目','打卡','','一家','这里','发现','疫情','一起','铁口','古里','太古','橘子洲','橘子','发现','喜欢','下午','昨天','疫情','一次','一下','购物','一直','回家','对面','第一','重庆','购物中心','大家','哈哈哈哈','已经','股份','好吃','天河','哈哈','哈哈哈','上海','不是','地铁门','这么','第一次','附近','但是','知道','还有','小区','城市','时间','每次','万象','广场','国金','广场','中心','万达','IFS','长沙','成都','广州','可以','天河城','大悦','很多','一个','看到','什么','就是','因为','我们','这个','不能','商场','真的','没有','今天','自己','现在','然后','时候','还是'}

result_list=[]
a=jieba.lcut(content)   #分词用  ,加上‘cut_all=True’ 为获取所有可能的词，有冗余
a=a+jieba.lcut(content1)
for word in a:
    if len(word)>1:      #一个字的词删了
        result_list.append(word)    
random.shuffle(result_list)    #弄乱顺序

wd=Counter(result_list)    #词频

b=" ".join(result_list)        #分词后为列表形式，此操作为拿出来重新为文本形式
for sw in stop:
    del wd[sw]

most=wd.most_common(300)
df=pd.DataFrame(most)   #转化框架方便
df.to_excel("D:\数据\python 代码\能用的小东西\练习类\cipin.xlsx",index=False)   

#加上contour_width=1,contour_color='steelblue',    为画出轮廓
w=WordCloud(background_color='white',width=1000,height=700,mask=image,
font_path='msyh.ttc',stopwords=stop,scale=15)


w.generate(b)
w_color=w.recolor(color_func=image_color)   #重新上色

plt.imshow(w)
plt.axis("off")
# plt.show()   #弹出图片

w.to_file('ciyun.png')

f.close()

