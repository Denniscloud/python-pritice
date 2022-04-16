'''
作用： 下载梨视频的视频
日期  2022年02月03日
'''

# 1,拿到conid
# 2，拿到videostatus返回的的json——》srcurl
# 3，srcurl里面的内容进行修整
# 4，下载视频

import requests
url="https://www.pearvideo.com/video_1726624"
conid=url.split("_")[1]

videosuatus=f"https://www.pearvideo.com/videoStatus.jsp?contId={conid}&mrd=0.2622845728606451"
print(videosuatus)

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.12151 SLBChan/101',
    'Referer': url
}
resp=requests.get(videosuatus,headers=headers)
dic=resp.json()
# print(dic)
srcurl=dic['videoInfo']['videos']['srcUrl']
sysemtime=dic['systemTime']
srcurl=srcurl.replace(sysemtime,f"cont-{conid}")
# print(srcurl)
# with open('a.mp4',mode="wb")as f:
#     f.write(requests.get(srcurl).content)

