import requests
'''
    下载渭南师范学院官网图片简单实例
'''
url = 'http://www.wntc.edu.cn/images/banner11.jpg'
headers = {
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}
response = requests.get(url, headers=headers)
if response.status_code == 200:
    with open('001.jpg', 'wb') as f:
        # w 写入模式
        # b 二进制
        f.write(response.content)