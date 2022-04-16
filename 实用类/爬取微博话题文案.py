'''
2022.2.27  16.39
试着爬取某个话题的文案  (长时间不用需要更新cookies)
'''

from lxml import etree
import requests
import time


def get_some(resp,i):
    html = etree.HTML(resp)
    # print(resp.text)
    divs=html.xpath('/html/body/div[1]/div[3]/div[2]/div[1]/div[1]/div')
    for div in divs:
        content=div.xpath('./div//div[1]/div[2]/p[1]/text()')
        content1="".join(content).strip(" ")
        f.write(content1)

    # f.write(f"\n{i}\n")
    time.sleep(1)

def get_url(titl,cook):
    for i in range(j):
        url=f"https://s.weibo.com/weibo/{titl}&page={i+1}"
        header={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.12151 SLBChan/101',
            'cookie':cook
        }
        print(f'第{i}页打好了')
        resp=requests.get(url,headers=header)
        page=resp.text

        get_some(page,i)
        resp.close()

f=open(r"能用的小东西/实用类/商场买什么.txt","a",encoding="utf-8")
# j=input("你想爬取多少页（建议50）")
j=47
titl='天河城'      #改 
cook='SINAGLOBAL=2450926147985.029.1642395905533; login_sid_t=8fd053a6fa4040c4d1869fbda98e4427; cross_origin_proto=SSL; _s_tentry=nsl.lenovo.com.cn; Apache=7709268453136.72.1648123338501; ULV=1648123338505:19:2:1:7709268453136.72.1648123338501:1646214229016; WBtopGlobal_register_version=2022032420; SSOLoginState=1648123535; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Whdz0Is28SEyKsc61WEpoPc5JpX5KMhUgL.Foe4eKqNSK5pS0.2dJLoI7fodsvf9Ffoqgf7dGH0; ALF=1680522562; SCF=AgplKIZnqljMWUU9BNlZK-_o97gKkn0ep_m0GOEXVOuGFKMyZxsgcvJ74lxLt7o-PyKC9RIH6dfTXtSO35SoBGM.; SUB=_2A25PTfmTDeRhGeVH6lQW9S7NzDWIHXVsO2xbrDV8PUNbmtAfLRTzkW9NT3rmLhgX7W2zu1gh31wfMj97qNmt9dfX; wvr=6; UOR=,,login.sina.com.cn; webim_unReadCount=%7B%22time%22%3A1648986601045%2C%22dm_pub_total%22%3A1%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A28%2C%22msgbox%22%3A0%7D; WBStorage=f4f1148c|undefined'

get_url(titl,cook)
f.close()

print("over!")
