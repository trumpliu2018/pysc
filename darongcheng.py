import requests
import time
import json
from wxpusher import WxPusher

app_token = 'xxx'   # 本处改成自己的应用 appToken
uid_myself = 'xxx'     # 本处改成自己的 UID

cookies=[
    {
        'name': 'trump7513',
        'auth':'Bearer xxx'
    },
]

def wxpusher_send(msg):
    result = WxPusher.send_message(msg,
                 uids=[uid_myself,],
                 token=app_token,
                 summary=msg[:999])
    return result

msgs = []
for i, auth in enumerate(cookies, start=1):
    name = auth['name']
    msg = f"\n=======开始执行账号{i} {name}======="
    print(msg)
    msgs.append(msg)
    url = "https://member.imixpark.com:48889/api/Sign/SignIn"https://github.com/trumpliu2018/pysc/tree/main
    payload = ""
    headers = {
    'Accept': 'application/json',
    'Authorization': auth['auth'],
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Referer': 'https://servicewechat.com/wx24d80b0b74d12b46/142/page-frame.html',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.45(0x18002d2c) NetType/WIFI Language/zh_CN',
    'buildingid': '80007'
    }
    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        msg = response.json()
        print(msg)
        if msg['success']: 
            msgs.append(msg['data']['giftmsg'])
        else:
            msgs.append(msg['msg'])
            

    except Exception as e:
        print(e)
        continue
    
   


if len(msgs)>0:
    wxpusher_send('大融城签到' + '\n'.join(msgs))
