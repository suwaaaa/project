import re

import requests


def GEThtmltxt(url):
    kv = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER'}
    try:
        r = requests.get(url, headers=kv, timeout=30)
        r.raise_for_status()
        r.encoding = "UTF-8"
        return r.text
    except:
        return "000"


def INFORMATION(names, links, unrepect_dates, html):
    all_name = re.findall(r'(?<= title=\").*?(?=\")', html)
    all_link = re.findall(r'(?<=a href=\").*?(?=\")', html)
    all_date = re.findall(r'(?<= alt=\").*?(?=\")', html)
    getname = []
    getlinks = []
    getdate = []
    for name in all_name:
        if re.findall(r'(GTA5百世代练|世$|于$| $|其他分享|GTA5辅助投稿|年|2020|GTA5免费辅助|卡任务栏|默认分类|LOGO|ATOM|RSS|RSD)', name):
            pass
        else:
            getname.append(name)
    for li in all_link:
        if re.findall(r'(java|feed|comment|start)', li):
            pass
        else:
            if re.findall(r'archives', li):
                getlinks.append(li)
    for date in all_date:
        if re.findall(r'(LOGO|GTA5|百世|关于|年|V|v|QQ|默认|教程|办法|辅助|其他|游戏)', date):
            pass
        else:
            getdate.append(date)
    unrepect_names = []
    unrepect_links = []
    unrepect_dates = []
    for l in getname:
        if l not in unrepect_names:
            unrepect_names.append(l)
    for l in getlinks:
        if l not in unrepect_links:
            unrepect_links.append(l)
    for l in getdate:
        if l not in unrepect_dates:
            unrepect_dates.append(l)
    for i in range(len(unrepect_dates)):
        dates.append(unrepect_dates[i].split(","))
    for i in range(max(len(unrepect_names), len(unrepect_links), len(unrepect_links))):
        names.append(unrepect_names[i].split(","))
        links.append(unrepect_links[i].split(","))


def makeit(new_names, new_links, new_dates):
    f = open("C:/Users/12645/Desktop/GTA5-最新辅助.txt", "w")
    tplt = "{:^90}\t{:^20}\t{:^90}"
    for i in range(min(len(new_names), len(new_links), len(new_dates))):
        f.write(tplt.format(new_names[i], new_dates[i], new_links[i]) + "\n")


if __name__ == '__main__':
    url = "https://www.138u.cn"
    html = GEThtmltxt(url)
    names = []
    links = []
    dates = []
    INFORMATION(names, links, dates, html)
    new_names = sum(names, [])
    new_links = sum(links, [])
    new_dates = sum(dates, [])
    makeit(new_names, new_links, new_dates)
