import requests

import time
import json
import os



class mp_spider(object):

    def __init__(self):
        self.offset = 10
        # self.base_url = 'https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz=MjM5MTQ4NjA3Nw==&f=json&offset={}&count=10&is_ok=1&scene=124&uin=MjA2MDM3NTU%3D&key=650e2cfea6c9072e3bf25bcb439b1bc6a95a5799eef6e214285502dc78df91c59ad60162f6e0136df5946d7c229ff486206541744d4fad13b7d2d2e2202d45d91e6bd7e81695c087135fbd59281d692a&pass_ticket=jAFRJRtWRdJcSXta5fiYsjBqfK6vqTIYWrULumuK5sc%3D&wxtoken=&appmsg_token=960_rOLbarjUKv9J0wPtj-6ucLdP9o4-av2_bfRoWQ~~&x5=0&f=json'
        # self.headers = {
        #     'Host': 'mp.weixin.qq.com',
        #     'Connection': 'keep-alive',
        #     'Accept': '*/*',
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.884.400 QQBrowser/9.0.2524.400',
        #     'X-Requested-With': 'XMLHttpRequest',
        #     'Referer': 'https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MjM5MTQ4NjA3Nw==&scene=124&uin=MjA2MDM3NTU%3D&key=2b903b9a7252346947b8c8bec6a8e97ea469a66c7c55196aec680d36fef8d99bdd51ba33c76a8d0e5655e5186714a09c18bdc873bdac2350ffd215c1d3cb331a3f67f0dcc00984035cbaacc19e1ef3e2&devicetype=Windows+10&version=62060344&lang=zh_CN&a8scene=7&pass_ticket=jAFRJRtWRdJcSXta5fiYsjBqfK6vqTIYWrULumuK5sc%3D&winzoom=1',
        #     'Accept-Encoding': 'gzip, deflate',
        #     'Accept-Language': 'zh-CN,zh;q=0.8,en-us;q=0.6,en;q=0.5;q=0.4',
        #     'Cookie': 'rewardsn=; wxtokenkey=777; wxuin=20603755; devicetype=Windows10; version=62060344; lang=zh_CN; pass_ticket=jAFRJRtWRdJcSXta5fiYsjBqfK6vqTIYWrULumuK5sc=; wap_sid2=COvG6QkSiAF0WmRTaHdBSmFwWUx4eWxmeXIzYVZ2RkpYMzZoMF8wa280bmpwMGF1NHhLamtFejdZUG5ZVmducnI4QjRFa1gzTVJYa0luRlhfS2RLTDhDVTk0eTNTUWNPd2hsa004eDV4bER1Uzg4WXhTTmRTN1pNYk9HOHpETERhbUo5ZnRUVHdBTUFBQX5+MPOS3tgFOA1AlU4='
        # }

        # 下面是stormzhang的公众号地址以及cookie
        self.base_url = 'https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz=MzA4NTQwNDcyMA==&f=json&offset={}&count=10&is_ok=1&scene=124&uin=MjA2MDM3NTU%3D&key=2b903b9a72523469de670030af99fbe5783162509e27e4c6bc8839f03ab4c01f99cb3107fabc35aa6d782af36605c7665263ac6cce37bab45dd6f16851624066e03a9aff437ba4e4249d7dc0be26a4ef&pass_ticket=N%2BsuWexcAtK1rOTYf4aLP3AgSP2cy3pVru7QKwqkEnM%3D&wxtoken=&appmsg_token=960_4UscgxzvuD3TK51LnPOvfeOFFtzwSdL1OUvOfw~~&x5=0&f=json'
        self.headers = {
            'Host': 'mp.weixin.qq.com',
            'Connection': 'keep-alive',
            'Accept': '*/*',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.884.400 QQBrowser/9.0.2524.400',
            'X-Requested-With': 'XMLHttpRequest',
            'Referer': 'https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MjM5MTQ4NjA3Nw==&scene=124&uin=MjA2MDM3NTU%3D&key=2b903b9a7252346947b8c8bec6a8e97ea469a66c7c55196aec680d36fef8d99bdd51ba33c76a8d0e5655e5186714a09c18bdc873bdac2350ffd215c1d3cb331a3f67f0dcc00984035cbaacc19e1ef3e2&devicetype=Windows+10&version=62060344&lang=zh_CN&a8scene=7&pass_ticket=jAFRJRtWRdJcSXta5fiYsjBqfK6vqTIYWrULumuK5sc%3D&winzoom=1',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-us;q=0.6,en;q=0.5;q=0.4',
            'Cookie': 'rewardsn=; wxtokenkey=777; wxuin=20603755; devicetype=Windows10; version=62060344; lang=zh_CN; pass_ticket=N+suWexcAtK1rOTYf4aLP3AgSP2cy3pVru7QKwqkEnM=; wap_sid2=COvG6QkSiAF0WmRTaHdBSmFwWUx4eWxmeXIzYVZ2RkpYMzZoMF8wa280bmpwMGF1NHhJVTBSRWN5RTNybmVUakc5NS1GQnVsRjdaWFdlY3E1YU5YQWlNbE5lWlppdjBHdTB5d2xPWEtaZ2czN0NnVzU0UmViMmRCUkhEZkVMYWZrWUhsMUE1aXdBTUFBQX5+MMaH39gFOA1AlU4='
        }
    def request_data(self):
        try:
            response = requests.get(self.base_url.format(self.offset), headers=self.headers)
            print(self.base_url.format(self.offset))
            if 200 == response.status_code:
               self.parse_data(response.text)
        except Exception as e:
            print(e)
            time.sleep(2)
            pass

    def parse_data(self, responseData):

            all_datas = json.loads(responseData)

            if 0== all_datas['ret']:

                summy_datas = all_datas['general_msg_list']
                datas = json.loads(summy_datas)['list']
                for data in datas:
                    try:
                        title = data['app_msg_ext_info']['title']
                        title_child = data['app_msg_ext_info']['digest']
                        article_url = data['app_msg_ext_info']['content_url']
                        cover = data['app_msg_ext_info']['cover']
                        print(title,title_child,article_url,cover)
                    except Exception as e:
                        print(e)
                        continue


                print('----------------------------------------')
                time.sleep(3)
                self.offset = self.offset+10
                self.request_data()
            else:
                print('抓取数据出错！')



if __name__ == '__main__':
    d = mp_spider()
    d.request_data()
