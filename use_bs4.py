from bs4 import BeautifulSoup
import requests

url = 'http://sj.zol.com.cn/bizhi/meinv/'
response = requests.get(url).text
# print(response.text)
soup = BeautifulSoup(response, 'lxml')
# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.find(id='globalSearch'))
# for link in soup.find_all('a'):
#     print(link.get('href'))
# tag的属性操作如同字典
# print(soup.find('li').string)
