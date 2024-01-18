import requests
import time
import json
from wxpusher import WxPusher

app_token = 'x'   # 本处改成自己的应用 appToken
uid_myself = 'x'     # 本处改成自己的 UID

cookies=[
    {
        'name': 'trump139',
        'cookie':''
    },
    {
        'name': 'trump 0865',
        'cookie':''
    },
    {
        'name': 'trump7513',
        'cookie':'
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
    msg = f"\n=======开始执行账号{i} {name}======="
    print(msg)
    msgs.append(msg)
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
        msgs.append(f'签到: {msg}')
    else:
        msgs.append(f'签到失败: {response}')
        print(f"签到失败{response}")
    
    # 获取任务列表
    msg = '获取任务列表'
    print(msg)
    url = 'https://act.you.163.com/act-attendance/task/list'
    url_reward = 'https://act.you.163.com/act-attendance/task/reward'
    url_trig = 'https://act.you.163.com/act-attendance/task/trigger'
    url_withdraw_info = 'https://act.you.163.com/act-attendance/att/v4/index'
    url_withdraw = 'https://act.you.163.com/act-attendance/att/v4/walk'
    headers['X-Requested-With']= 'XMLHttpRequest'
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        tasks= response.json()['data']['dailyTasks']
        for task in tasks:
            body = {'taskId': task['taskId']}
            if task['status'] == 0:

                msg = f'开始做: {task["title"]}'
                print(msg)
                msgs.append(msg)
                headers['Content-Type']='application/json'
                if task['taskType'] == 18:          
                    response = requests.request("POST", url_reward, headers=headers, data=json.dumps(body))
                    print(response.text)
                elif task['taskType'] == 4:
                    response = requests.request("POST", url_trig, headers=headers, data=json.dumps(body))
                    print(response.text)
                    if response.json()['success'] is True:
                        time.sleep(1)
                        response2 = requests.request("POST", url_reward, headers=headers, data=json.dumps(body))
                        print(response2.text)
                        pass
                elif task['taskType'] == 2:
                    url_read = f'https://act.you.163.com/act/pub/ssr/RXiKIIZTw64X.html?appConfig=1_1_1&taskId={task["taskId"]}&taskType=2&redirectUrlRequire=10&fr=sc'
                    requests.request("GET", url_read, headers=headers, data=payload)
                    time.sleep(11)
                    response2 = requests.request("POST", url_reward, headers=headers, data=json.dumps(body))
                    print(response2.text)
            else:
                headers['Content-Type']='application/json'
                response2 = requests.request("POST", url_reward, headers=headers, data=json.dumps(body))
                print(response2.text)
        
        info = requests.request("GET", url_withdraw_info, headers=headers, data=payload)
        cnt = info.json()['data']['game']['remainStepCount']
        if cnt and cnt > 0:
            for i in range(cnt):
                time.sleep(2)
                msg = f'第{i+1} 次抽奖'
                print(msg)
                msgs.append(msg)
                response = requests.request("GET", url_withdraw, headers=headers, data=payload)
                reward = response.json()
                msg = f'获得 {reward["data"]}'
                print(msg)
                msgs.append(msg)
            pass

    else:
        print(f"获取任务列表失败{response}")


if len(msgs)>0:
    wxpusher_send('\n'.join(msgs))
