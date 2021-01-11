def getnum():
    nums = []
    inumstr = input("entre numbers please:")
    while inumstr != '':
        nums.append(eval(inumstr))
        inumstr = input("enter again:")
    return nums


def mean(numbers):  # 计算平均值
    s = 0.0
    for num in numbers:
        s += num
    return s / len(numbers)


def dev(numbers, mean):  # 计算方差
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num - mean) ** 2
    return pow(sdev / (len(numbers) - 1), 0.5)


def medium(numbers):  # 计算中位数
    sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        med = (numbers[size // 2 - 1] + numbers[size // 2]) / 2
    else:
        med = numbers[size // 2]
    return med


import time

n = getnum()
m = mean(n)
print("平均值{}，方差:{}，中位数:{}".format(m, dev(n, m), medium(n)))
time.sleep(60)
