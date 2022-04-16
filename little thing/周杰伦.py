'''
作用： 打出周杰论的网页
日期  2022年01月12日
'''
import requests
url="https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=monline_4_dg&wd=周杰伦"
header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0"}
res=requests.get(url,headers=header)
print(res.text)
res.close()