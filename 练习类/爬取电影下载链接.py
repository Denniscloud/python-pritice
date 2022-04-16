'''
作用： 爬取电影下载链接
日期  2022年02月01日
'''
import requests
import re
import csv

doman="https://www.dytt8.net/index2.htm"
doman2="https://www.dytt8.net/"
resp=requests.get(doman,verify=False)    #verify证书失效
resp.encoding='gbk'     #采用适当的解码方式 没写的时候默认”ulf-8“
# print(resp.text)
obj1=re.compile(r'手机浏览.*?(?P<dat>.*?)<!--}end:最新电影下载--->',re.S)
result1=obj1.finditer(resp.text)
for i in result1:
    dat=i.group('dat')

obj2=re.compile(r"<a href='(?P<href>.*?)'.*?</tr>.*?<tr>",re.S)
result2=obj2.finditer(dat)
hrelist=[]    #建立列表
for it in result2:
    child=doman2+it.group('href')   #把两个数据粘在一起 整个链接拼接起来
    hrelist.append(child)  # 把链接列表保存下来
# print(hrelist)
downloadlist=[]
obj3=re.compile(r'◎译　　名(?P<moive>.*?)<br />.*?href="(?P<download>.*?)">',re.S)
f=open("电影链接.csv",mode="w")
csvwriter=csv.writer(f)
for itt in hrelist:
    childresp=requests.get(itt, verify=False)
    childresp.encoding='gbk'
    result3=obj3.finditer(childresp.text)
    for ii in result3:
        down=ii.group("moive")+ii.group("download")
        downloadlist.append(down)
        dic=ii.groupdict(f)
        csvwriter.writerow(dic.values())
        # print(ii.group("moive"))
        # print(ii.group("download"))
f.close()
print("OVER!!")