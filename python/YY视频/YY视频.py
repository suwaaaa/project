import parsel
import requests

url = "http://www.win4000.com/meinvtag26_1.html"
myheader = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36 Edg/86.0.622.43'}
respond = requests.post(url=url, headers=myheader)
getdata = respond.text
# print(respond.text)


myselect = parsel.Selector(getdata)
# print(myselect)
url_list = myselect.xpath('//div[@class="Left_bar"]//ul/li/a/@href').getall()
# print(dataurl)

for data in url_list:
    # print(data)
    respond2 = requests.get(url=data, headers=myheader).text

    myselect2 = parsel.Selector(respond2)
    photo_url = myselect2.xpath('//div[@class="pic-meinv"]//a/img/@data-original').get()

    img = requests.get(url=photo_url, headers=myheader).content

    # 存儲
    file_name = photo_url.split('/')[-1]
    # print(file_name)

    with open('D:/files/YY图片/' + file_name, mode='wb') as f:
        f.write(img)
        print("数据导入成功:", file_name)
