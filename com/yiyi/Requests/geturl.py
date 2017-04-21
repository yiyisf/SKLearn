import requests
from io import BytesIO



headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch, br',
    'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.6,en;q=0.4',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}

url = 'http://127.0.0.1:8081/extracode?t=1492737820163'

r = requests.get(url, headers=headers)
# print(r.text)
#
# print(r.cookies.keys())
#
# print(r.cookies.values())



