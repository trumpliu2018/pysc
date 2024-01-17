'''
    抓包 shiwanxing.com， 所有cookie填入ciyi，多账号@隔开
'''
import os
import requests
import time
from wxpusher import WxPusher

app_token = ''   # 本处改成自己的应用 appToken
uid_myself = ''     # 本处改成自己的 UID

def wxpusher_send(msg):
    result = WxPusher.send_message(msg,
                 uids=[uid_myself,],
                 token=app_token,
                 summary=msg[:999])
    return result

accounts = os.getenv('ciyi')
if accounts is None:
    print('no cookie for ciyi haoyangmao')
    exit()
else:
    accounts_list = os.environ.get('ciyi').split('@')
    num_of_accounts = len(accounts_list)
    print(f"获取到 {num_of_accounts} 个账号")
    for i, account in enumerate(accounts_list, start=1):
        print(f"\n=======开始执行账号{i}=======")
        url = "https://shiwanxing.com/s4/lite.subtask.list?_uts=11874736&ts=1705389329098"
        payload = ""        
        headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Cookie': account,
        'Origin': 'https://shiwanxing.com',
        'Referer': 'https://shiwanxing.com/v4/dashboard',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 version=1.3.1 bid=com.cdjk.ciyi tk=2',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"'
        }
        # response = requests.post(url, headers=headers, json=data)
        response = requests.request("GET", url, headers=headers, data=payload)
        if response.status_code == 200:
            tasks = response.json()['payload']['tasks']
            print(f'get {len(tasks)} tasks:')
            if len(tasks) > 0:
                for task in tasks:
                    if task['qty'] > 0:
                        if task['reward_map']['kabi']['total_reward'] != '':
                            title = task['title']
                            id = task['id']
                            quality = task['qty']
                            t = int(time.time()*1000)
                            print(f'开始任务：{title}, id :{id}')
                            task_url = f'https://shiwanxing.com/s4/lite.subtask.start?task_id={id}&quality={quality}&t_mark=6d4c5a&times=1&ts={t}'
                            print(task_url)
                            response = requests.request("GET", task_url, headers=headers, data=payload)
                            result = response.json()['payload']
                            print(result)
                            msg = result['message']
                            code = result['type']
                            if code == 0:
                                print(f'抢到任务：{title}, id :{id}')
                                wxpusher_send(f'ciyi:抢到任务：{title}, id :{id}')
                                break
                            else:
                                print(msg)
        else:
            print(f"获取任务失败{response}")
