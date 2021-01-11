import parsel
import requests

url = "https://www.138u.cn/"
headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36 Edg/86.0.622.43'}
respond = requests.get(url=url, headers=headers)
respond.raise_for_status()
respond.encoding = "UTF-8"
data = respond.text

select1 = parsel.Selector(data)
title = select1.xpath('//div[@class="card-deck"]//div/a/img/@alt').getall()

select2 = parsel.Selector(data)
photo_url = select2.xpath('//div[@class="card-deck"]//div/a/img/@data-original').getall()

for each, i in zip(photo_url, title):
    MyPhoto = requests.get(url=each, headers=headers, timeout=50).content

    with open('../辅助爬取/Photoes/' + i + '.jpg', mode="wb") as f:
        f.write(MyPhoto)
        print(i + "成功了")
print("------finished------")
