# -*- coding: UTF-8 -*-

'''
用米游社cookie获取原神抽卡记录链接的authkey
2022/10/09
'''

import requests
import time
import random
import hashlib
import string
import json
import urllib.parse
import os


#输入米游社cookie
cookies = input('输入米游社cookie:')

headers={'cookie':cookies}

url='https://webapi.account.mihoyo.com/Api/login_by_cookie?t='

account_info=requests.get(url+str(int(time.time()*1000)),headers=headers).json()

print(account_info)

account_id = account_info['data']['account_info']['account_id']
url='https://api-takumi.mihoyo.com/auth/api/getMultiTokenByLoginTicket?login_ticket={}&token_types=3&uid={}'.format(account_info['data']['account_info']['weblogin_token'],account_id)

r=requests.get(url,headers=headers)
token_list=r.json()['data']['list']
#print(token_list)

str1=f'stuid={account_id}; '
str2=''

for d in token_list:
    str2 += f'{d["name"]}={d["token"]}; '
str1 += str2
str1 += cookies
#print(str1)

url = 'https://api-takumi.mihoyo.com/binding/api/getUserGameRolesByCookie?game_biz=hk4e_cn'
r  = requests.get(url, headers={'cookie':str1})
print(r.text)

#列表里有米游社绑定的所有原神账号信息
game_info = r.json()['data']['list']

#有多个原神账号
if game_info == []:
    print('没有绑定原神账号，请先去米游社绑定')
    input()
    os.exit()
elif len(game_info) > 1 :
    print('有多个原神账号，请选择：')
    for i,v in enumerate(game_info):
        print(f"{i+1}.uid:{v['game_uid']} 昵称:{v['nickname']}")
    select = int(input('请输入序号：'))
    game_info = game_info[select-1]


game_uid = game_info['game_uid']
game_biz = game_info['game_biz']
region = game_info['region']
#print(game_uid, game_biz, region)

# 随机文本
def random_text(num: int) -> str:
    return ''.join(random.sample(string.ascii_lowercase + string.digits, num))

def md5(text: str) -> str:
    md5 = hashlib.md5()
    md5.update(text.encode())
    return md5.hexdigest()

def getDs():
    n = 'ulInCDohgEs557j0VsPDYnQaaz6KJcv5'
    #n = 'dWCcD2FsOUXEstC5f9xubswZxEeoBOTc'
    i = str(int(time.time()))
    r = random_text(6)
    c = md5("salt=" + n + "&t=" + i + "&r=" + r)
    return f"{i},{r},{c}"


headers={'Content-Type':'application/json; charset=utf-8',
        'Host':'api-takumi.mihoyo.com',
        'Accept':'application/json, text/plain, */*',
        'Referer':'https://webstatic.mihoyo.com',
        'x-rpc-app_version':'2.28.1',
        'x-rpc-client_type': '5',
        'x-rpc-device_id': 'CBEC8312-AA77-489E-AE8A-8D498DE24E90',
        'x-requested-with': 'com.mihoyo.hyperion',
        'DS':getDs(),
        'Cookie':str1,
      }


data = {'auth_appid':'webview_gacha',
        'game_biz':game_biz,
        'game_uid':game_uid,
        'region':region}

#print(data)

#获取authkey
r = requests.post('https://api-takumi.mihoyo.com/binding/api/genAuthKey',headers=headers,json=data)
#print(r.text)

authkey = r.json()['data']['authkey']
#print(authkey)

#print(urllib.parse.quote(authkey))

#authkey需要url编码
gacha_url = 'https://webstatic.mihoyo.com/hk4e/event/e20190909gacha-v2/index.html?win_mode=fullscreen&authkey_ver=1&sign_type=2&auth_appid=webview_gacha&init_type=200&timestamp={}&lang=zh-cn&device_type=mobile&plat_type=android&region={}&authkey={}&game_biz={}#/log'.format(int(time.time()),region,urllib.parse.quote(authkey),game_biz)

print(gacha_url)
input()
