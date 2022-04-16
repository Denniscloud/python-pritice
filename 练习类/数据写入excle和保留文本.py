'''
把爬进来的csv文件的一条条文本进行情感分析
得出的值放入excle文本中

'''
import snownlp
import pandas as pd
import openpyxl as op



f_csv=open("D:\数据\python 代码\能用的小东西\练习类\comment1.csv","r")
f_txt=open("D:\数据\python 代码\能用的小东西\练习类\data.txt","a+")
a=[]
items=[]
mydata=[]

for i in f_csv:
    
    i=i.replace('\n',' ')  
    a.append(i.split(','))

print("开始进行情感分析")
for each in a:
    each=','.join(each)   #把数据从列表拿出来去除列表然后变成文本
    items.append(each)
    each_word=snownlp.SnowNLP(each)
    feeling=each_word.sentiments
    mydata.append(feeling)
    # csvwriter.writerow(feeling)

data=[items,mydata]
dfData = {  # 用字典设置DataFrame所需数据
        '项目': data[0],
        '数据': data[1]
    }
 
df=pd.DataFrame(dfData)
# print(dfData)
df.to_excel("D:\数据\python 代码\能用的小东西\练习类\data3.xlsx",index=False)


for j in a:
    # print(j)
    f_txt.write(','.join(j)+'\n')


f_csv.close()
f_txt.close()
print("大哥搞定！！")
