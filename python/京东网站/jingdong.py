import requests

url = "https://item.jd.com/2967929.html"
try:
    r = requests.get(url)
    r.raise_for_status()
    text = r.text
    r.encoding = r.apparent_encoding
    print(text[:1000])
except:
    print("error")
