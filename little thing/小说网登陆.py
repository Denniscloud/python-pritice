'''
作用： 小说网站登陆（login未找到，未完成）已解决
日期  2022年01月16日
'''
# 登陆-》得到cooki
# 带着cookie去请求书架的url  得到书架的内容
# 把两个操作连接起来
# 我们可以使用session 进行请求  session是一连串的请求在整个过程中cookie不会丢失

import requests

# 连续的会话，保存上一次的内容
session=requests.session()
data={
    "loginName": "19980823731",
    "password": "qwe123456"
}
header={
    'Cookie': 'GUID=81e07838-3516-409d-ae85-872e5475081b; c_channel=0; c_csc=web; Hm_lvt_9793f42b498361373512340937deb2a0=1642321329,1642321362,1642493644; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F01%252F81%252F38%252F88343881.jpg-88x88%253Fv%253D1642321698000%26id%3D88343881%26nickname%3D%25E4%25B9%25A6%25E5%258F%258Bk3vU532Z7%26e%3D1658046753%26s%3Ddfef382199e68724; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2288343881%22%2C%22%24device_id%22%3A%2217e61fabcd3a1e-04982a07cec678-50594155-1327104-17e61fabcd48ed%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%2281e07838-3516-409d-ae85-872e5475081b%22%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1642495169'
}
# 1，先登录
url="https://passport.17k.com/ck/user/login"
session.post(url,data=data)
# print(resp.text)
# print(resp.cookies)

# 2，拿书架上的数据
# 刚才的session有cookie
resp=session.get('https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919')
print(resp.json())

# 方法二(用get)
#
# resp=requests.get("https://www.zhihu.com/collection/653598877",headers=header)




