import requests
import re
#! 下一步分页提取链接
#！ 可将各个网页链接存放在列表里
url = 'http://www.wntc.edu.cn/xb/szzy/zwsjk.htm'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}
r = requests.get(url,headers=headers)
r.encoding = 'utf-8'
    # # 由于python默认编码格式为utf-8，而网页编码格式和其本身格式可能不一致
    # # 解决中文编码问题
    # print(r.encoding)
    # # 网页编码格式：utf-8
    # print(r.apparent_encoding)
    # # 网页头部声明格式：UTF-8-SIG
# pattern = re.compile('href=\\"(.*)\\"\\stitle=\\"(.*?)\\"')
pattern = re.compile('<td valign="top" width="387" style=".*"><p><a (href="http://.*") .*>(.*)</span></a></p></td>')
    # 加一个括号可以单独提取出父条件里的子条件
    # 如果超链接格式不整齐，可以把前缀包括进去，我真是个天才！
html = r.text
result = pattern.findall(html)
# for link in result:
#     print(link)
# print(type(link))
# 此处link为tuple，需要转换数据结构，否则不能进行写入操作

with open('links.txt','w',encoding='utf-8') as f:
    for link in result:
        f.writelines(str(link) + '\n')
            #将元组写入文件，字典同理
            
# 如果pattern只用一次，也可使用下面写法：
# result = re.findall('href=\\"(.*)\\.htm\\"\\stitle=\\"(.*?)\\"',html)
