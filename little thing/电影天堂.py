'''
作用： 爬取电影天堂的某个栏目的（在其他地方已成功，保留原型）
日期  2022年01月12日
'''
#1 ，定位2021必看篇     !!!(前提是页面源代码里出现所想要的数据)
#2，从2021必看篇中提取到子页面的链接地址
#3，请求子页面的链接地址，拿到我们想要的下载地址  /html/gndy/dyzz/20220112/62202.html

import requests
import re
doman="https://www.dytt8.net/index2.htm"
doman2="https://www.dytt8.net/"
resp=requests.get(doman,verify=False)    #verify证书失效
resp.encoding='gbk'     #采用适当的解码方式 没写的时候默认”ulf-8“
#print(resp.text)

obj1=re.compile(r"最新影片推荐.*?<ul>(?P<dat>.*?)</ul>",re.S)
result1=obj1.finditer(resp.text)
for i in result1:
    dat=i.group('dat')
#第二步，提取出来
#  a href=    存放的是超链接
obj2=re.compile(r"<a href='(?P<href>.*?)'.*?</tr>.*?<tr>",re.S)
result2=obj2.finditer(resp.text)
hrelist=[]    #建立列表
for it in result2:
    child=doman2+it.group('href')   #把两个数据粘在一起 整个链接拼接起来
    hrelist.append(child)  # 把链接列表保存下来

obj3=re.compile(r'◎片　　名(?P<moive>.*?)<br />.*?<a target="_blank" href="(?P<download>.*?)">',re.S)
for itt in hrelist:
    childresp=requests.get(itt, verify=False)
    childresp.encoding='gb2312'
    #print(childresp.text)
    result3=obj3.finditer(childresp.text)
    print(result3.group("moive"))
    print(result3.group("download"))
    break



