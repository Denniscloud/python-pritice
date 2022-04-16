'''
作用：爬取百度网页
日期  2022年01月12日
'''

from urllib.request import urlopen
url="https://blog.csdn.net/ktsmeb/article/details/119269043?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522164371409416781683931211%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=164371409416781683931211&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_click~default-1-119269043.first_rank_v2_pc_rank_v29&utm_term=urlopen&spm=1018.2226.3001.4187"
res=urlopen(url)

# encoding="utf-8" ，必写 因：默认“utf-8”，需要加上encoding="utf-8"
with open("baidu.html", mode="w", encoding="utf-8") as feil:
    feil.write(res.read().decode("utf-8"))
print("over")