
from lxml import etree
import requests
import time
import re

def get_mid(url):     #获取mid
    resp=requests.get(url,headers=headers)
    mid_re=re.compile("mid=(?P<mid>\d+)",re.S)
    mid=mid_re.search(resp.text).group("mid")
    print(mid)
    return mid


def get_comment(mid,ref_url):      #获取评论
    url='https://weibo.com/aj/v6/comment/big' 
    parm={ 
        'ajwvr': 6,                                    
        'id': mid,
        'from': 'singleWeiBo',
        '__rnd': int(time.time()*1000)
    }

    headers["referer"]=ref_url     #headers之后加上防止封号
    headers["x-requested-with"]="XMLHttpRequest"
    n_url=url   #  搞一下
    n=1
    while 1:
        resp=requests.get(n_url,params=parm,headers=headers)
        # print(resp.text)  #第一页评论信息
        #解析评论信息
        html=resp.json()['data']['html']
        # print(html)
        if n_url:
            n_url=url+"?"+process_common(html,n)   #下一个url 
            n+=1
        else:
            break


def process_common(hm,n):     #解析评论
    tree=etree.HTML(hm)

    divs=tree.xpath("//div[@class='list_box']/div/div[@node-type='root_comment']")
    for div in divs:
        comment_id=div.xpath("./@comment_id")
        user=div.xpath("./div[2]/div[1]/a/text()")
        content=div.xpath("./div[2]/div[1]/text()")
        content="".join(content).strip().strip("： ")    #去除空格，去除：去掉列表框
        user=user[0]
        comment_id=comment_id[0]
        f.write(comment_id)
        f.write("|||")
        f.write(user)
        f.write("|||")
        f.write(content)
        f.write("\n")
        # print(comment_id, user, content)
    f.write("============第"+str(n)+"页评论=============\n")
    print(f'打印{n}页')
        
    # 拿到actiondata  有下一页的cookie
    action_data=tree.xpath("//div[@node-type='comment_loading']/@action-data")
    # print(action_data)
    if action_data:   #如果拿不到action—data,找其他的
        url=action_data[0]
        url+="&__rnd="+str(int(time.time()*1000))
        url+="&ajwvr=6"
        url+="&from=singleWeiBo"
        return url
    
    
    # action_data1=re.findall(r'action-type="reply" action-data="(.*?)"',hm)
    # # print(action_data1)
    # if action_data1:   #如果拿不到action—data,找其他的
    #     for i in action_data1:
    #         dat=i
    #         dat+="&__rnd="+str(int(time.time()*1000))
    #         dat+="&ajwvr=6"
    #         dat+="&from=singleWeiBo"
    #         print(dat)
            
    #         get_hidecomment(mid,dat)
    #         print("sucees")
            
            

    loading_url=tree.xpath("//a[@action-type='click_more_comment']/@action-data")
    if loading_url:
        url=loading_url[0]
        url+="&__rnd="+str(int(time.time()*1000))
        url+="&ajwvr=6"
        url+="&from=singleWeiBo"
        return url
    return None

def get_hidecomment(mid,dat):      #获取评论
    url2='https://weibo.com/aj/v6/comment/big'
    print("sucees1")
    parm={ 
        'ajwvr': 6,                                    
        'id': mid,
        'from': 'singleWeiBo',
        '__rnd': int(time.time()*1000)
    }
    n_url=url2+"?"+dat
    headers["referer"]=n_url    #headers之后加上防止封号
    headers["x-requested-with"]="XMLHttpRequest"
    
    resp1=requests.get(n_url,params=parm,headers=headers)
        # print(resp.text)  #第一页评论信息
        #解析评论信息
    html1=resp1.json()['data']['html']
    tree=etree.HTML(html1)
      #下一个url 
    divs=tree.xpath("//div[@class='list_box']/div/div[@node-type='root_comment']")
    for div in divs:
        comment_id1=div.xpath("./@comment_id")
        user1=div.xpath("./div[2]/div[1]/a/text()")
        content1=div.xpath("./div[2]/div[1]/text()")
        content1="".join(content1).strip().strip("： ")    #去除空格，去除：去掉列表框
        user1=user1[0]
        comment_id1=comment_id1[0] 
        print(comment_id1, user1, content1)
        continue
     
    
cooke='SINAGLOBAL=2450926147985.029.1642395905533; login_sid_t=8fd053a6fa4040c4d1869fbda98e4427; cross_origin_proto=SSL; _s_tentry=nsl.lenovo.com.cn; Apache=7709268453136.72.1648123338501; ULV=1648123338505:19:2:1:7709268453136.72.1648123338501:1646214229016; SSOLoginState=1648123535; wvr=6; XSRF-TOKEN=O0LRwtQpRcd_s0peyVPzgE06; SCF=AgplKIZnqljMWUU9BNlZK-_o97gKkn0ep_m0GOEXVOuGZQQK-ZdN7unwv1zH3QtpvE8cBL4cGFUYXKDMurmJkgI.; SUB=_2A25PObr9DeRhGeVH6lQW9S7NzDWIHXVsTqs1rDV8PUNbmtAKLUbfkW9NT3rmLoBR8riPDH6MZ2cQxaZwEsxsFH7_; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Whdz0Is28SEyKsc61WEpoPc5JpX5KMhUgL.Foe4eKqNSK5pS0.2dJLoI7fodsvf9Ffoqgf7dGH0; ALF=1679752748; WBPSESS=ymQQvZfiEgNlXqkHLclU2vduYMqijQ9XlfIZIPANnneM5ZyzHcYjfKNZGDW6EN76MS97SbENZZ0ehfgc26D0S-6rjIuP7Pm_SgDT3KdG-tCtchIN6UqagiHGsH1b3EaYlRCYQEzZGRhWL1xlAUTQqQ==; wb_view_log_3916750179=1536*8641.25; UOR=,,nsl.lenovo.com.cn; webim_unReadCount=%7B%22time%22%3A1648216841002%2C%22dm_pub_total%22%3A1%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A42%2C%22msgbox%22%3A0%7D'

headers={
    "Cookie": cooke,
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.12151 SLBChan/101'
}

f=open('评论.txt',mode="a",encoding="utf-8")
url='https://weibo.com/2656274875/Lllgyd3Hs?filter=hot&root_comment_id=0&type=comment'
# url=input("输入网址：注意格式规范：：")
# https://weibo.com/7467277921/LgFcVhNlj?type=comment
#https://weibo.com/1728148193/LgZjan9ST?type=comment#_rnd1645713357870
mid=get_mid(url)
get_comment(mid,url)
print("over!!!")   
f.close()

