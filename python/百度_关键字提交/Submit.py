import requests

params = {'wd': "Python"}
url = "http://www.baidu.com/s"
r = requests.get(url=url, params=params)
r.raise_for_status()
text = r.text

print(text[:1000])
