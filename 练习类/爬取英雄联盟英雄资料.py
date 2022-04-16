'''
爬取159个英雄的资料及技能，背景故事，技能

有时间可以试试爬取图片的信息
'''

import requests

url='https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js?ts=2743129'
resp=requests.get(url)
dic=resp.json()
print(dic)

for i in dic['hero']:
    hero_id=i['heroId']  #第一次请求拿到各个英雄的id，方便定位英雄
    url1='https://game.gtimg.cn/images/lol/act/img/js/hero/{}.js?ts=2743129'.format(hero_id)   #嵌入id，目前这种方法能用
    resp1=requests.get(url1)       #二次请求拿到单独放英雄的全部数据
    hero=resp1.json()
    hero_name=hero['hero']['name'] +"--"+hero['hero']['title']        #用字典的方式获取到名字，下同

    f=open(f"heroimformation/{hero_name}.txt",mode='w',encoding='utf-8')    #打开文件
    f.write("英雄：\n")        #往文件写入东西
    f.write(hero_name+'\n\n')

    stroy=hero['hero']['shortBio']
    f.write("背景故事：\n")
    f.write(stroy+'\n\n')
    
    f.write("技能：\n")
    for s in hero['spells']:
        s_key=s['spellKey']
        s_des=s['description']
        s_name=s['name']
        f.write(s_name+'\n')
        f.write('快捷键：'+s_key+'\n')
        f.write('技能描述：'+s_des+'\n')
        f.write("==================================\n\n")
    f.close()
    resp1.close()

resp.close()
print("大哥,搞定!!")