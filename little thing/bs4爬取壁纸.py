'''
作用： bs4爬取壁纸 （未完成）
日期  2022年01月12日
'''
#1 ，定位2021必看篇     !!!(前提是页面源代码里出现所想要的数据)
#2，从2021必看篇中提取到子页面的链接地址
#3，请求子页面的链接地址，拿到我们想要的下载地址

import requests
from bs4 import BeautifulSoup
import time
url = "https://www.umei.cc/bizhitupian/weimeibizhi/"
head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.12151 SLBChan/101'}
resp = requests.get(url,headers=head)
resp.encoding = 'utf-8' #处理乱码
#print( resp.text)
#把源代码交给bs
main_page = BeautifulSoup(resp.text,"html.parser")
alist = main_page.find("div", class_="TypeList") .find_all("a")
print(alist)
for a in alist:
    href = a.get('href')#直接通过get就可以拿到属性的值
    # #拿到子页面的源代码
    child_page_resp =requests.get(href)
    child_page_resp.encoding = 'utf-8'
    child_page_text = child_page_resp.text
    #从子页面中拿到图片的下载路径
    child_page = BeautifulSoup(child_page_text,"html.parser")
    p = child_page.find( "p",align="center")
    img = p.find( "img")
    src = img.get("sre")
    # 下载图片
    img_resp = requests.get(src)
    # img_resp.content#这里拿到的是字节
    img_name = src.split("/")[-1]  # 拿到url中的最后一个/以后的内容
    with open ( "img/"+img_name,mode="wb") as f:
        f.write(img_resp.content)  # 图片内容写入文件
    print("over! ! ! ",img_name)
    time.sleep(1)  #打印完一个休息一秒，防止崩溃
print("all over! ! ! ")

