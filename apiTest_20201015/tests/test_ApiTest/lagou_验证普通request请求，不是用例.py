# 验证请求拉钩网，不是用例

import requests

url = 'https://gate.lagou.com/v1/entry/message/newMessageList'
cookies = {
    '_gid': 'GA1.2.995205387.1602684316',
    'gate_login_token': '3e13c425a062fafb9099f9320e1da36dc0eb1673834d6dfb'

}
headers = {
    'x-l-req-header': '{deviceType: 9}'
}

res = requests.session().get(url=url, cookies=cookies, headers=headers)

print(res.content.decode('utf-8'))
