import time as ti

import requests


def getwebsite(url):
    try:
        r = requests.get(url, timeout=25)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("有点问题啊,老弟")


def calculate_time():
    begin = ti.perf_counter()
    for i in range(100):
        getwebsite(url)
    t = ti.perf_counter() - begin
    print("it had spent:{}".format(t))


if __name__ == "__main__":
    url = "http://www.baidu.com"
    calculate_time()
