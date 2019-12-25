import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Mobile Safari/537.36'
}
loginData = {
    
}
url = 'http://10.0.1.1:9090/zportal/loginForWeb?wlanuserip=3a5f24920b2f6943b39e83697d1fea1b&wlanacname=32f0f26760cab6f993970dcbf67f8292&ssid=a50667e3f7d4e25110e7a7c3d5387950&nasip=5abe2afa7924490f2a8fa53014c04b9d&snmpagentip=&mac=bcee13f05ee288583832d29d74be8046&t=wireless-v2&url=56fbdadc6ac57d97f8cae07ac4ea3ddcb35c6a7bdf97bf09524cb32ef93b1572745b5900a15b8046&apmac=&nasid=32f0f26760cab6f993970dcbf67f8292&vid=4e6e7100e79ae557&port=1358e32049ead34a&nasportid=a25b45948c15af402f7109d202bf26f22ce175da9b9c9ba40f18f1d8e8edf33e'
response = requests.post(url,header=headers,data=)