'''
作用： 百度翻译
日期  2022年02月01日
'''
import  requests
S=input("请输入你要翻译的单词")
url="https://fanyi.baidu.com/sug"
dreams={
    'kw': S
}
resp=requests.post(url,data=dreams)
print(resp.json())

