# from urllib import request
# url = 'http://www.baidu.com'
# response = request.urlopen(url,timeout=2)
# print(response.read().decode=('utf-8'))

# 打印状态码
# import urllib.request
# response = urllib.request.urlopen('http://www.baidu.com')
# print(response.status)

# ！！！关于data参数，未理解
# import urllib.parse
# import urllib.request
# data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
# response = urllib.request.urlopen('http://httpbin.org/post', data=data)
# print(response.read())

# # timeout参数实例
# import socket 
# import urllib.request
# import urllib.error
# try:
#     response = urllib.request.urlopen('http://httpbin.org/get',timeout= 0.1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason, socket.timeout):
#         print("TIME OUT")

# URLerror报错
# from urllib import request,error
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

# try:
#     response = request.urlopen('http://cuiqingcai.com/index.htm',timeout=1)
# except error.URLError as e:
#     print(e.reason)

# 捕捉错误
# from urllib import request,error
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
# try:
#     response = request.urlopen('http://cuiqingcai.com/index.htm',timeout=1)
# except error.HTTPError as e:
#     print(e.reason, e.code, e.headers, sep='\n')
# # 由于URLError是HTTPError的父类，所以可以先捕捉子类错误再捕捉父类错误
# except error.URLError as e:
#     print(e.reason)
# else:
#     print("Request Successfully")

# URL解析parse
# from urllib.parse import urlparse
# # result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
# result = urlparse('www.baidu.com/index.html', scheme='http', allow_fragments=True)
# print(type(result),result)
# # scheme=协议，netloc=域名，path=路径,params=参数,query=查询,fragment=片段

# urlencode 将字典转换为url参数
# from urllib.parse import urlencode
# params = {
#     'name': 'Jerome',
#     'age': 22
# }
# base_url = 'www.baidu.com?'
# url = base_url + urlencode(params)
# print(url)

# quote解决中文编码问题
# from urllib.parse import quote
# keyword = '壁纸'
# url = 'http://wwww.baidu.com/s?wd=' + quote(keyword)
# print(url)

# unqote解码
# from urllib.parse import unquote
# url = 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
# print(unquote(url))

# requests库的使用
# import requests
# r = requests.get('https://wwww.baidu.com')
# print(type(r))
# print(r.status_code)
# print(type(r.text))
# print(r.text)
# print(r.cookies)

# 向requests库请求添加字典参数
# import requests
# data = {
#     'name': 'jerome',
#     'age': 22
# }
# r = requests.post('http://httpbin.org/post', params=data)
# print(r.text)

# 爬取GitHub图标
# import requests
# r = requests.get('https://github.com/favicon.ico')
# with open('favicon.ico', 'wb') as f:
#     f.write(r.content)

# 爬取知乎发现页
# import requests
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
# }
# r = requests.get("https://www.zhihu.com/explore", headers=headers)
# print(r.text)

# 校验码
# import requests
# r = requests.get('https://www.jianshu.com')
# exit() if not r.status_code == requests.codes.ok else print("Successfully")

# 上传文件
# import requests
# files = {'file': open('try.py', 'rb')}
# r = requests.post('http://httpbin.org/post', files=files)
# print(r.text)

# 获取cookies
# import requests
# r = requests.get('https://www.baidu.com')
# print(r.cookies)
# for key, value in r.cookies.items():
#     print(key + '=' + value) 

# Cookies登陆哔哩哔哩
# import requests
# headers = {
#     'Cookie': "CURRENT_FNVAL=16; buvid3=55D204EB-D685-40FF-ABBE-4B1ACDA551FB40771infoc; stardustvideo=1; rpdid=|(um|R))mRJ|0J'ullmR)R~Ym; fts=1561127853; LIVE_BUVID=AUTO8615611278762882; CURRENT_QUALITY=64; _uuid=7A6E51F5-DFA9-2F81-2B76-9838BCADF53A60414infoc; __51cke__=; sid=53a7ltp3; DedeUserID=436858701; DedeUserID__ckMd5=0b19535cf4ac3968; SESSDATA=8585cf36%2C1566468015%2C39dbbb71; bili_jct=62cf096f0e2dbb0e542a3386a0939ce9; UM_distinctid=16c1e46992c267-07154d0beecfa3-37607c05-13c680-16c1e46992f230; __tins__19988117=%7B%22sid%22%3A%201563978281712%2C%20%22vd%22%3A%204%2C%20%22expires%22%3A%201563981654609%7D; __51laig__=12",
#     'Host': 'www.bilibili.com',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
# }
# r = requests.get('https://www.bilibili.com', headers=headers)
# print(r.text)   

# 取消ssl证书验证
# import requests
# r = requests.get('https://www.12306.cn', verify=False)
# print(r.status_code)

# 取消警告提示
# import requests
# from requests.packages import urllib3
# urllib3.disable_warnings()
# r = requests.get('https://www.12306.cn', verify=False)
# print(r.status_code)

# 正则表达式01-match及基础语法
# import re
# content = 'Hello 123 4567 World_This is a Regex Demo'
# print(len(content))
# result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}',content) 
# """ 
# ^   匹配字符串的开头 ^hello匹配以hello开头的字符串
# \s  匹配空白字符
# \d  匹配任意数字
# {4} 复制前面的表达式4遍
# \w  匹配字母、数字及下划线
# """
# print(result)
# print(result.group())
# print(result.span())

