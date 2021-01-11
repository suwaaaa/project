import bs4
import requests
from bs4 import BeautifulSoup


def gettext(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fillunivlist(uinfo, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr("td")
            uinfo.append([tds[0].string, tds[1].string, tds[3].string])


def printunivlist(uinfo, num):
    f = open("中国大学排名——爬虫.txt", "w")
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    f.write(tplt.format("排名", "学校", "总分", chr(12288)) + "\n")
    for i in range(num):
        u = uinfo[i]
        f.write(tplt.format(u[0], u[1], u[2], chr(12288)) + "\n")


def main():
    uinfo = []
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2018.html"
    html = gettext(url)
    fillunivlist(uinfo, html)
    printunivlist(uinfo, 20)


main()
