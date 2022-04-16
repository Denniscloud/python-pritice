'''
作用： bs4 的简单介绍+实战操作爬取html存在数据
日期  2022年01月12日
'''
import requests
from bs4 import BeautifulSoup
import csv
url ="https://www.construdip.com/"
resp=requests.get(url)
f=open("菜价.csv",mode="w")
csvwrite=csv.writer(f)

#解析数据
#1，把页面源代码交给BeautifulSoup进行处理，生成bs对象
page = BeautifulSoup(resp.text,"html.parser")   #指定html解析器
# print(page)
# 2，从bs4对象查找数据
# find（标签，属性=值）   找第一个返回
# find_all（标签，属性=值）     全部找出来


# table = page.find("table", class_="hq_table") # class是python的关键字 #  class_    下划线_ 是为了区分关键字和属性的区别
table = page.find("table", attrs={"class":"hq_table"}) #和上一行是一个意思。此时可以避免class
# #拿到所有数据行
trs = table.find_all("tr")[1:]
for tr in trs:#每一行
    tds = tr.find_all( "td")#拿到每行中的所有td·
    name=tds[0].text  #.text 表示拿到被标签标记的内容
    Low = tds[1].text  # .text 表示拿到被标签标记的内容
    avg = tds[2].text # .text 表示拿到被标签标记的内容
    high = tds[3].text #.text表示拿到被标签标记的内容
    gui = tds[4].text # .text表示拿到被标签标记的内容
    kind = tds[5].text # .text 表示拿到被标签标记的内容
    date = tds[6].text # .text表示拿到被标签标记的内容
    # print(name,low,avg,high,gui, kind,date)
    csvwrite.writerow([name, Low, avg, high, gui, kind, date])

f.close()
print("over!!")





