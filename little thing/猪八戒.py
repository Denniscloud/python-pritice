'''
作用： 猪八戒网爬取表格信息
日期  2022年01月12日
'''

import requests
from lxml import etree

url = "https://wuzhou.zbj.com/search/f/?kw=spss"
header={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.12151 SLBChan/101'
}
resp = requests.get(url,headers=header)

print(resp.text)
#解析
html = etree.HTML(resp.text)

#拿到每一个服务商的div
print(html)        
divs = html.xpath("/html/body/div[6]/div/div/div[2]/div[6]/div/div")
print(divs)
for div in divs:
    name=div.xpath("./div//a[1]/div[1]/p/img/text()")
    # //*[@id="utopia_widget_76"]/a[2]/div[2]/div[1]/span[1]
    price=div.xpath("./div//a[2]/div[2]/div[1]/span[1]/text()")[0].strip("￥")  #去掉￥符号
    title="spss".join(div.xpath("./div/a[2]/div[2]/div[2]/p/text()"))      #使spss从原来的.转化为原数据并拼接起来
    print(name,price,title)


