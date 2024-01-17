import requests
import time
from wxpusher import WxPusher

app_token = 'AT_pGJXhP8fb5GtAj1UNzPuFBHyGMLLurmZ'   # 本处改成自己的应用 appToken
uid_myself = 'UID_CkXdtKXbmE6swDhjKClRe5l4Luk5'     # 本处改成自己的 UID

cookies=[
    {
        'name': 'trump139',
        'cookie':'yx_csrf=f951331eb405d4251d344cb6cf22daa4; yx_userid=26225722347; yx_username=yd.0db3daafe65c4c7ea%40163.com; yx_sid=c9b3e904-6a54-48b7-bacf-6f122ce91839; NTES_OSESS=U66mCCCiO9v7lAPnSgMcJM3eGhCmS7ohsgFYFCnpYC5A00UG7IMJSOEYz0yGw_Eoq3TCloJAB0K3G0jKAy8Xxi6GSJFjpkzGpKVaJLxlFuPbgaeDg3WkRXa._HbNmCMfILFTDrMM.zqJpn6GRqYfZ_.yiYKaChQcF4Ah7HTzWKD2v3pEeXZRilIF9baWXviyaBNLMNqTMfFclUshC2UXOJY85aBF4HuZn1VvYwmKnA6BMJLEf5OA3FFSr; P_OINFO=oep2jt_fm32671ecfe456efadbf23e872ddec0f6fb@wx.163.com|1705457163|0|yanxuan|00&99|null&null&null#zhj&330100#10#0#0|&0|yanxuan|oep2jt_fm32671ecfe456efadbf23e872ddec0f6fb@wx.163.com; S_OINFO=1705457163|0|##|oep2jt_fm32671ecfe456efadbf23e872ddec0f6fb@wx.163.com|; yx_aui=5d2d8d9e-4847-4ca2-9bf9-4f038babf38b'
    },
    {
        'name': 'trump 0865',
        'cookie':'yx_curusername=yd.6ff32df182bc4e6f9@163.com; yx_s_device=964c453-cad7-9aae-2410-b8269ed031; yx_s_tid=tid_web_851ffd8c488542b3b0536939ef45b1bf_712db2bf0_1; yx_userid=26259703735; yx_username=yd.6ff32df182bc4e6f9@163.com; YX_SUPPORT_WEBP=0; yx_but_id=21ca1dfef5284409b088c86f982c55a13f2e4e70639226bd_v1_nl; NTES_YD_SESS=taL6.OFsTEcF7MLcAU9PdzqwmpUZwTM9i4KR_HQzios_nx2OnJy7pc0.rE1l6MVeLTnZvv1slSCBkhWszcrTh0FrqzUvP3Ti7dPL9AvL4s.EfEyMmMHfYXHEtg7HmhUXzf0zMyEWMaz6ebEIdh0dV4INWi1Kf9dgxt40n8mWqUWJeSOx2W7Z3B90sEIxSf2_0uFy5UgVi829_9S1jK3EAKxdxHwOvpK6O; P_INFO=17321030865|1705461725|0|yanxuan|00&99|shh&1705461725&yanxuan#zhj&330100#10#0#0|&0|null|17321030865; S_INFO=1705461725|0|0&60##|yd.6ff32df182bc4e6f9|; yx_aui=3c690055-e359-443c-9198-7fe777b85e05; yx_csrf=cbda122a66430d0f4810029ddaf49f83; yx_csrf=244afae49dbd743bc4a342d4a65fd72f; yx_new_sid=26259703735_1705461770571_us8E7G; yx_sid=c313b935-c269-4c2f-9932-d180e386df16; _bl_uid=nelUnrv7hUt7gUvnXj9wl4R8FwbF'
    },
    {
        'name': 'trump7513',
        'cookie':'yx_userid=53354470; yx_aui=ae45b50f-b5a3-448a-876b-8b304d6f109c; yx_app_type=android; yx_app_channel=aos_market_xiaomi; yx_csrf=88907f917ad5e845fa45981057d26a0e; _bl_uid=1alLOodtppsuIdg7h7FquIsop7pb; YX_SUPPORT_WEBP=1; yx_but_id=3abc325d3964423ca0444be52fe4db6daa5075c275d45d4b_v1_nl; NTES_YD_SESS=BHEeMrLIeMdXGg5joQJCjDB2syZ6ySRlvRaE9S8VbPz9krW0kCD17oEV56RE8kKgWoGYutPm.Ks31133P7g5eYrIHgFxQNNaOMjO38OdpAGS.rTEPmXBwk7TBn1S.mKYV_NVlDTMlOVwfJTiemNe6RixMbUa_cenr9y4mDS6QyLoJUvY6ZfqNE_6dqxJNinVYfvanb1mrFuljfJBTNybxi76gfVcYfQFN; S_INFO=1705446487|0|0&60##|yd.991bfa3ae3e2447aa|; P_INFO=17721067513|1705446487|0|yanxuan|00&99|zhj&1703646268&yanxuan#zhj&330100#10#0#0|&0||17721067513; yx_new_sid=53354470_1705446490827_yAWGlD; yx_curusername=yd.991bfa3ae3e2447aa@163.com; yx_s_device=a751e0f-a16a-5866-a2b7-5b4ad64e91; yx_s_tid=tid_web_1ba77cdf558b4afdaf3691e1d4fa76d5_f469d3783_1; yx_username=oep2jt_m0ad1abf7c64d4be02a3f92dab753ae4958%40wx.163.com; yx_sid=640c164d-6d52-44c6-9f8b-67696de9ff34'
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

