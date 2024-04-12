"""
还没写好，不能调用，安装amazfit就可以用手机注册。然后用zeep life(原小米运动) 绑定支付宝和微信就好
"""

import time
import requests
import re
from fake_useragent import UserAgent

# ua = str(UserAgent().random)
ua = UserAgent(verify_ssl=False, use_cache_server=False, cache=False).random
print(ua)


class XiaomiSport:
    def __init__(self, phone: str, password: str, step: int):
        # 手机号
        self.cookie = None
        self.headers0 = None
        self.headers1 = None
        self.csrf_token = None
        self.phone = '+86' + phone
        # 密码
        self.password = password
        # 修改步数
        self.step = step
        self.url0 = "http://118.195.237.33"
        self.url1 = "http://118.195.237.33/changeXiaomiSteps"
        self.regex_csrf_token = re.compile('<input id="csrf_token" name="csrf_token" type="hidden" value="(.*?)">',
                                           re.S)
        self.sess = requests.session()

    def parse_html0(self):
        self.headers0 = {
            'User-Agent': ua,
        }
        resp = self.sess.get(self.url0, headers=self.headers0, allow_redirects=False)
        print(resp.status_code, "第一次get")
        print(resp.cookies.values()[0], '第一次的cookies')
        self.cookie = 'session=' + resp.cookies.values()[0]
        html0 = resp.content.decode()

        self.csrf_token = self.regex_csrf_token.findall(html0)[0]
        print(self.csrf_token, '第一次的到的token')

        if self.csrf_token:
            return self.csrf_token

    def parse_html1(self):
        self.parse_html0()
        print(self.cookie, '第二次的cookie')
        self.headers1 = {
            'User-Agent': ua,
            'Referer': 'http: // 118.195.237.33/',
            'Cookie': self.cookie
        }

        time.sleep(1)
        self.data1 = {
            'csrf_token': self.csrf_token,
            'phone': self.phone,
            'password': self.password,
            'steps': self.step,
        }
        resp = self.sess.post(self.url1, data=self.data1, headers=self.headers1, allow_redirects=False)
        print(resp.status_code, "第一次get")
        html1 = resp.content.decode()
        print(html1)

    def run(self):
        # self.parse_html0()
        self.parse_html1()


if __name__ == '__main__':
    spider = XiaomiSport('edgar_ye@petalmail.com', 'ycy12569800', 11064)
    spider.run()
#         eyJfZnJlc2giOmZhbHNlLCJjc3JmX3Rva2VuIjoiNDJmOWZiN2NmNTIxNTJiNGY3Mjg0Y2FlYTc2NzUwNmJhNDM4NDBkYSJ9.Y2ZVsA.n0Fv8fdYo8nlIZ8rtmLTY7QBlO8
# session=eyJfZnJlc2giOmZhbHNlLCJjc3JmX3Rva2VuIjoiMmFmZDhkNDBlZGY2NTQyNTRlNTliM2Y4ZTI4NTZkYjlmMzllY2M4NyJ9.Y2YfDg.QADH_nFFjg4GgqmMenY1V4Sgmck
