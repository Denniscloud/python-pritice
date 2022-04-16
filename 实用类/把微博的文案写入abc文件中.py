'''
作用： 把微博的文案写入abc中，（第一次运行需要清空abc文件）
日期  2022年01月19日
'''
import requests
import re
url='https://s.weibo.com/weibo?q=冬奥会'
# url=input("请输入链接")
header={
    'cookie': 'SINAGLOBAL=2450926147985.029.1642395905533; _s_tentry=weibo.com; Apache=9456433494903.96.1642560292898; ULV=1642560292931:4:4:4:9456433494903.96.1642560292898:1642497025358; SCF=AgplKIZnqljMWUU9BNlZK-_o97gKkn0ep_m0GOEXVOuGPKqje3JCRomlyvNt1y1iR9qrlBok_fidqiMFCj9xYEQ.; SUBP=0033WrSXqPxfM72wWs9jqgMF55529P9D9Whdz0Is28SEyKsc61WEpoPc5JpVF02RS0MNShnReoec; SUB=_2AkMWuwbbdcPxrABYmf4SyWvja4RH-jylbm8tAn7uJhMyAxh77n8jqSVutBF-XEgoPV5LWnBnfCUrOjE5XmnLGI_j'
}
resp=requests.get(url=url,headers=header)
# print(resp.text)
lis=re.compile(r'<p class="txt" node-type=".*?" nick-name=(?P<nei>.*?)</p>',re.S)
result=lis.finditer(resp.text)

# print(resp.text)

for i in result:
    print(i.group("nei"))
    f=open("abc.txt", 'a', encoding='utf-8')
    f.write(i.group("nei"))
f.close()
print("over!!")