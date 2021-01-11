import pprint

import requests

url = "https://www.amazon.cn/?tag=baidhydrcnnv-23&ref=GS_sw_baidu_pc_ymxppc_0465"
headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36 Edg/86.0.622.43'}

r = requests.get(url=url, headers=headers)
r.encoding = r.apparent_encoding
r.raise_for_status()
text = r.text
pprint.pprint(text[1000:2000])
