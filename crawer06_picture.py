'''
    爬取优美网图片
'''
import requests
import re
import urllib.request


def download_img():
    url = 'http://www.umei.cc/weimeitupian/oumeitupian/'
    html = requests.get(url)
    html.encoding = 'utf-8'
    if html.status_code == 200:
        pattern = re.compile('http://i1.whymtj.com/uploads/.*.png')
        paths = '../Codes/downloads/'
        x = 0
        img_urls = pattern.findall(html.text)
        for img in img_urls:
            urllib.request.urlretrieve(img,'{0}{1}.png'.format(paths,x))
            x = x + 1
download_img()
