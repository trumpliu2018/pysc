import os
import requests
import time
from wxpusher import WxPusher

app_token = ''   # 本处改成自己的应用 appToken
uid_myself = ''     # 本处改成自己的 UID
cookies=[
    {
        'name': 'trump139',
        'cookie':''
    },
    {
        'name':'trump0865',
        'cookie':''
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
    url = " https://ob.shike.com/shike/api/appList?download=1&asin=qLgKdimlcEyWodmfE6wMBDWAf3yBgvk0L%2BHqm%2FBfvkBWuIdqUl5Vaw05uWqCc5o4C9Ey9lR9QMSsdEzDpIIJnPN2K9XQYuebVZSFeDNLPiBzXLTHFjon2TSiob74aKoIcGFcogoyDt5yVcq64bT%2BIcZOSzC6LqsH2dXDnqawegIROZJKy07KUjlf67yBstoK07ha2Co3cA0LY3kVYF%2F5s%2BJyd3XEg5MaF3ZAm5D8e4ewBL1OQ83sCxmseaRw7Xu5jAUIbDWcthOFOSRPq2auy%2Bh7GN7Y6haGBwx3R%2BUgutr%2Fof09iSqqQPguIWC97nGFqYzRDYo9WmyixcT70QwnCgT%2BXoxoMLsmJyzZmM0pUvTuPNckzEp2r1MX%2F79%2BDPzjZqOn22IxtLO3BsaqpwhipA%3D%3D&wg=-1"
    payload = {}
    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'OD=y+t+bZtyU6ZBUFckkusYRMWWBVhgwsvFFnZ4FhWpj3jqyvEgRfa2wSMOFqK9uypV; _ga_VEJNHVRQC8=GS1.1.1705469965.30.1.1705470143.0.0.0; _ga=GA1.1.931568196.1704852364; Hm_lpvt_5fe1ea55c0fff327cca35a17fd50c576=1705469965; Hm_lvt_5fe1ea55c0fff327cca35a17fd50c576=1705368720,1705387101,1705420384,1705469965; JSESSIONID=BFE5B63CE2FFBE0B86297EB9126F25EE; ; OD=y+t+bZtyU6ZBUFckkusYRMWWBVhgwsvFFnZ4FhWpj3jqyvEgRfa2wSMOFqK9uypV',
    'Referer': 'https://ob.shike.com/',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Host': 'ob.shike.com',
    'Accept-Encoding': 'gzip, deflate, br'
    }
    # response = requests.post(url, headers=headers, json=data)
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        tasks = response.json()['data']['app']
        print(f'get {len(tasks)} tasks:')
        if len(tasks) > 0:
            for task in tasks:
                if task['notFree'] is False:
                        sign = task['sign']
                        t = int(time.time()*1000)
                        print(f'开始任务：{sign}')
                        data = {
                            'sign': sign,
                            'asin': 'qLgKdimlcEyWodmfE6wMBDWAf3yBgvk0L%2BHqm%2FBfvkBWuIdqUl5Vaw05uWqCc5o4C9Ey9lR9QMSsdEzDpIIJnPN2K9XQYuebVZSFeDNLPiBzXLTHFjon2TSiob74aKoIcGFcogoyDt5yVcq64bT%2BIcZOSzC6LqsH2dXDnqawegIROZJKy07KUjlf67yBstoK07ha2Co3cA0LY3kVYF%2F5s%2BJyd3XEg5MaF3ZAm5D8e4ewBL1OQ83sCxmseaRw7Xu5jAUIbDWcthOFOSRPq2auy%2Bh7GN7Y6haGBwx3R%2BUgutr%2Fof09iSqqQPguIWC97nGFqYzRDYo9WmyixcT70QwnCgT%2BXoxoMLsmJyzZmM0pUvTuPNckzEp2r1MX%2F79%2BDPzjtuyM6VMWhT6saEG2DRS1JQ%3D%3D'
                        }
                        h = {
                            'Accept': 'application/json, text/plain, */*',
                            'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
                            'Connection': 'keep-alive',
                            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
                            'Cookie': 'OD=y+t+bZtyU6ZBUFckkusYRMWWBVhgwsvFFnZ4FhWpj3jqyvEgRfa2wSMOFqK9uypV; _ga_VEJNHVRQC8=GS1.1.1705472296.31.1.1705472810.0.0.0; _ga=GA1.1.931568196.1704852364; Hm_lpvt_5fe1ea55c0fff327cca35a17fd50c576=1705469965; Hm_lvt_5fe1ea55c0fff327cca35a17fd50c576=1705368720,1705387101,1705420384,1705469965; JSESSIONID=BFE5B63CE2FFBE0B86297EB9126F25EE; _ga_VEJNHVRQC8=deleted',
                            'Origin': 'https://ob.shike.com',
                            'Referer': 'https://ob.shike.com/',
                            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
                            'Host': 'ob.shike.com',
                            'Accept-Encoding': 'gzip, deflate, br',
                            'Content-Length': '541'
                            }
                        url = f"https://ob.shike.com/shike/api/appClick?sign={sign}&asin=qLgKdimlcEyWodmfE6wMBDWAf3yBgvk0L%2BHqm%2FBfvkBWuIdqUl5Vaw05uWqCc5o4C9Ey9lR9QMSsdEzDpIIJnPN2K9XQYuebVZSFeDNLPiBzXLTHFjon2TSiob74aKoIcGFcogoyDt5yVcq64bT%2BIcZOSzC6LqsH2dXDnqawegIROZJKy07KUjlf67yBstoK07ha2Co3cA0LY3kVYF%2F5s%2BJyd3XEg5MaF3ZAm5D8e4ewBL1OQ83sCxmseaRw7Xu5jAUIbDWcthOFOSRPq2auy%2Bh7GN7Y6haGBwx3R%2BUgutr%2Fof09iSqqQPguIWC97nGFqYzRDYo9WmyixcT70QwnCgT%2BXoxoMLsmJyzZmM0pUvTuPNckzEp2r1MX%2F79%2BDPzjtuyM6VMWhT6saEG2DRS1JQ%3D%3D"
                        print(url)
                        res = requests.request("POST", url, headers=headers, data=payload)
                        fetch_res = res.json()
                        if fetch_res['code'] == '0':
                            print(f'试客 抢任务成功：{desc}')
                            wxpusher_send(f'{name} 抢任务成功：{desc}')
                            break
                        else:
                            msg =fetch_res['desc']
                            print(f'抢任务失败：{msg}')
                        time.sleep(10)
                pass
            pass
    else:
        print(f"获取任务失败{response}")
