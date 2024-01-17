import requests
import time
from wxpusher import WxPusher

app_token = 'xxx'   # 本处改成自己的应用 appToken
uid_myself = 'xxxx'     # 本处改成自己的 UID

cookies=[
    {
        'name': 'trump139',
        'cookie':'cookie3'
    },
    {
        'name': 'trump0865',
        'cookie:'cookie2':
    },
    {
        'name': 'trump7513',
        'cookie':'cookie3'
    }
]

def wxpusher_send(msg):
    result = WxPusher.send_message(msg,
                 uids=[uid_myself,],
                 token=app_token,
                 summary=msg[:999])
    return result

msgs = []
for i, cookie in enumerate(cookies, start=1):
    name = cookie['name']
    print(f"\n=======开始执行账号{i} {name}=======")
    url = "https://act.you.163.com/act-attendance/att/v3/sign"
    payload = ""
    headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': cookie['cookie'],
    'Referer': 'https://act.you.163.com/act/pub/ssr/HysmFsmeKj88.html?appConfig=1_1_2',
    'Accept-Encoding': 'gzip, deflate, br',
    'X-Requested-With': 'X-Requested-With',
    'Host': 'act.you.163.com'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        task= response.json()
        print(task)
        msg=task['msg']
        msgs.append(f'网易严选，账号{name}: {msg}')
    else:
        print(f"签到失败{response}")
if len(msgs)>0:
    wxpusher_send('\n'.join(msgs))

