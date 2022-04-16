
#    提取图片颜色让词云的颜色随图片颜色变化

from wordcloud import WordCloud,ImageColorGenerator
import matplotlib.pyplot as plt
# 安装jieba模块，凌晨安装效果比较好，因为网速
import jieba
import imageio 

image=imageio.imread('picture\购物女.jpg')
content=open(r"能用的小东西/实用类/商场买什么.txt","r",encoding="utf-8").read()
stop={'最近','晚上','地铁口','项目','好吃','但是','知道','还有','小区','城市','时间','每次','万象','广场','国金','广场','中心','万达','IFS','长沙','成都','广州','可以','天河城','大悦','很多','一个','看到','什么','就是','因为','我们','这个','不能','商场','真的','没有','今天','自己','现在','然后','时候','还是'}

result_list=[]
a=jieba.lcut(content)   #分词用  ,加上‘cut_all=True’ 为获取所有可能的词，有冗余

for word in a:
    if len(word)>1:      #一个字的词删了
        result_list.append(word) 
b=" ".join(result_list)        #分词后为列表形式，此操作为拿出来重新为文本形式


#加上contour_width=1,contour_color='steelblue',    为画出轮廓

w=WordCloud(background_color='white',width=1000,height=700,mask=image,
font_path='msyh.ttc',stopwords=stop,scale=15)

image_color=ImageColorGenerator(image)   #提取颜色
w.generate(b)
w_color=w.recolor(color_func=image_color)   #重新上色

plt.imshow(w_color)
plt.axis("off")
plt.show()   #弹出图片

w_color.to_file('shangchang.png')


