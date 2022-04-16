
import requests
import urllib
import base64
import time
import re
import json
import rsa
import binascii

header={
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Referer': 'https://weibo.com/login.php',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.12151 SLBChan/101'
    }
class Login(object):
    session=requests.session()
    user_name='18777488236'
    pass_word='qwe123456'

    def get_username(self):

        return base64.b64encode(urllib.parse.quote(self.user_name).encode("utf-8")).decode("utf-8")

    def get_pre_login(self):
        # int(time.time()*1000)
        params={
            'entry': 'weibo',
        'callback': 'sinaSSOController.preloginCallBack',   
        'su': self.get_username(),
        'rsakt': 'mod',
        'checkpin': '1',
        'client': 'ssologin.js(v1.4.19)',
        '_': int(time.time()*1000)
            }
        try:
            response=self.session.post("https://login.sina.com.cn/sso/prelogin.php",params=params,headers=header,verify=False)
            return json.loads(re.search(r"\((?P<data>.*)\)",response.text).group("data"))
        except:
            print("获取公钥失败")
            return 0

    def get_password(self):
        
        publiy_key=rsa.PublicKey(int(self.get_pre_login()["pubkey"],16),int("10001",16))
        password_string=str(self.get_pre_login()["servertime"])+'\t'+str(self.get_pre_login()["nonce"])+'\n'+self.pass_word
        return binascii.b2a_hex(rsa.encrypt(password_string.encode("utf-8"),publiy_key)).decode("utf-8")
        

    def login(self):
        post_data={
            "entry": "weibo",
        "gateway": "1",
        "from":"",
        "savestate": "7",
        "qrcode_flag": "false",
        "useticket": "1",
        "vsnf": "1",
        "su": self.get_username(),
        "service": "miniblog",
        "servertime": self.get_pre_login()["servertime"],
        "nonce": self.get_pre_login()["nonce"],
        "pwencode": "rsa2",
        "rsakv": self.get_pre_login()["rsakv"],
        "sp": self.get_password(),
        "sr": "1536*864",
        "encoding": "UTF-8",
        "prelt": "44",
        "url": "https://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack",
        "returntype": "TEXT"
        }

        login_data=self.session.post("https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.19)",data=post_data,headers=header,verify=False)
        print(login_data.text)

        
login=Login()
login.login()