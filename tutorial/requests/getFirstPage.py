# 获取首页
import requests
import re


ss = requests.session()
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Host': 'modao.cc',
    'Origin': 'https://modao.cc',
    'Referer': 'https://modao.cc/signin',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}

urls = 'https://modao.cc/sessions'

firstUrl = 'https://modao.cc/signin'


def gettoken():
    rs = ss.get(firstUrl)
    t = re.compile('name=\"authenticity_token\" value=\"(.*)\"', flags = 0)
    return t.findall(rs.text)


param = {
    'utf8': '✓',
    'authenticity_token': gettoken()[0],
    'email': 'yiyi119120@gmail.com',
    'password': '@zgxliuzhe'
}



rs = ss.post(urls, data=param)
#
print(rs.status_code)

print(rs.text)
# print(rs.cookies)
# print(rs.cookies.keys())

# print(gettoken()[0])