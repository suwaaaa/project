# #编程模板中给出了一个字符串，其中包含了含有重复的人名，请直接输出出现最多的人名。
# s = '''双儿 洪七公 赵敏 赵敏 逍遥子 鳌拜 殷天正 金轮法王 乔峰 杨过 洪七公 郭靖
#        杨逍 鳌拜 殷天正 段誉 杨逍 慕容复 阿紫 慕容复 郭芙 乔峰 令狐冲 郭芙
#        金轮法王 小龙女 杨过 慕容复 梅超风 李莫愁 洪七公 张无忌 梅超风 杨逍
#        鳌拜 岳不群 黄药师 黄蓉 段誉 金轮法王 忽必烈 忽必烈 张三丰 乔峰 乔峰
#        阿紫 乔峰 金轮法王 袁冠南 张无忌 郭襄 黄蓉 李莫愁 赵敏 赵敏 郭芙 张三丰
#        乔峰 赵敏 梅超风 双儿 鳌拜 陈家洛 袁冠南 郭芙 郭芙 杨逍 赵敏 金轮法王
#        忽必烈 慕容复 张三丰 赵敏 杨逍 令狐冲 黄药师 袁冠南 杨逍 完颜洪烈 殷天正
#        李莫愁 阿紫 逍遥子 乔峰 逍遥子 完颜洪烈 郭芙 杨逍 张无忌 杨过 慕容复
#        逍遥子 虚竹 双儿 乔峰 郭芙 黄蓉 李莫愁 陈家洛 杨过 忽必烈 鳌拜 王语嫣
#        洪七公 韦小宝 阿朱 梅超风 段誉 岳灵珊 完颜洪烈 乔峰 段誉 杨过 杨过 慕容复
#        黄蓉 杨过 阿紫 杨逍 张三丰 张三丰 赵敏 张三丰 杨逍 黄蓉 金轮法王 郭襄
#        张三丰 令狐冲 赵敏 郭芙 韦小宝 黄药师 阿紫 韦小宝 金轮法王 杨逍 令狐冲 阿紫
#        洪七公 袁冠南 双儿 郭靖 鳌拜 谢逊 阿紫 郭襄 梅超风 张无忌 段誉 忽必烈
#        完颜洪烈 双儿 逍遥子 谢逊 完颜洪烈 殷天正 金轮法王 张三丰 双儿 郭襄 阿朱
#        郭襄 双儿 李莫愁 郭襄 忽必烈 金轮法王 张无忌 鳌拜 忽必烈 郭襄 令狐冲
#        谢逊 梅超风 殷天正 段誉 袁冠南 张三丰 王语嫣 阿紫 谢逊 杨过 郭靖 黄蓉
#        双儿 灭绝师太 段誉 张无忌 陈家洛 黄蓉 鳌拜 黄药师 逍遥子 忽必烈 赵敏
#        逍遥子 完颜洪烈 金轮法王 双儿 鳌拜 洪七公 郭芙 郭襄 赵敏'''
# ls = s.split()
# search = {}
# for i in ls:
#     search[i] = search.get(i,0) + 1
# name,times = "",0
# for j in search:
#     if search[j] > times:
#         name,times = j,search[j]
# print(name)


# # 生成包含大小写字母、数字的随机密码 ?????????????
# import random
# import string
#
# random.seed(0)
#
#
# def generate_password(length):
#
#
# #
#
# print(generate_password(5))
# print(generate_password(8))
# print(generate_password(10))


# 打印输出附件文件的平均列数，计算方法如下：‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬
# （1）有效行指包含至少一个字符的行，不计算空行；‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬
# （2）每行的列数为其有效字符数；‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬
# （3）平均列数为有效行的列数平均值，采用四舍五入方式取整数进位。

# #文本的平均列数
# f = open("D:/files/latex.log")
# s, c = 0, 0
# for line in f:
#     line = line.strip("\n")
#     if line == "":
#         continue
#     s += len(line)
#     c += 1
# print(round(s / c))


# #获得用户的任何可能输入，将其中的英文字符进行打印输出，程序不出现错误。
# word = input()
# list = []
# for i in range(26):
#     list.append(chr(ord("a") + i))
#     list.append(chr(ord("A") + i))
# for i in word:
#     if i in list:
#         print(i,end="")

# 获得用户输入的一个数字，可能是浮点数或复数，如果是整数仅接收十进制形式，且只能是数字。
# 对输入数字进行平方运算，输出结果。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬
# 要求：‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬
# （1）无论用户输入何种内容，程序无错误；‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬
# （2）如果输入有误，请输出"输入有误"。
# s = input()
# # try:
# #     if complex(s) == complex(eval(s)):
# #         print(pow(eval(s),2))
# # except:
# #     print("输入有误")


# 获取系统的递归深度、当前执行文件路径、系统最大UNICODE编码值等3个信息，并打印输出。
# import sys
# print("RECLIMIT:{}, EXEPATH:{}, UNICODE:{}".
#       format(sys.getrecursionlimit(), sys.executable, sys.maxunicode))


# tabulate能够对二维数据进行表格输出，是Python优秀的第三方计算生态。
# from tabulate import tabulate
# data = [ ["北京理工大学", "985", 2000], \
#          ["清华大学", "985", 3000], \
#          ["大连理工大学", "985", 4000], \
#          ["深圳大学", "211", 2000], \
#          ["沈阳大学", "省本", 2000], \
#     ]
# print(tabulate(data,tablefmt="grid"))

# 无空隙回声输出 获得用户输入，去掉其中全部空格，将其他字符按收入顺序打印输出。
# a = input()
# for i in a:
#     if i == " ":
#         pass
#     else:
#         print(i,end="")

# 关键行指一个文件中包含的不重复行。关键行数指一个文件中包含的不重复行的数量。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬
# 统计附件文件中与关键行的数量。
# dict ={}
# # with open('latex.log','r',encoding='utf-8')as f:
# #     lines = f.readlines()
# #     for line in lines:
# #         rline = line
# #         dict[rline]=dict.get(rline,0)+1
# # print('共{:}关键行'.format(len(dict)))


# 读入一个字典类型的字符串，反转其中键值对输出。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬
# 即读入字典key:value模式，输出value:key模式。
# s = input()
# try:
#     d = eval(s)
#     e = {}
#     for k in d:
#         e[d[k]] = k
#     print(e)
# except:
#     print("输入错误")


# 附件是《沉默的羔羊》中文版内容，请读入内容，分词后输出长度大于2且最多的单词。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬
# 如果存在多个单词出现频率一致，请输出按照Unicode排序后最大的单词。
# import jieba
# txt = open("D:/files/沉默的羔羊.txt","r",encoding='utf-8').read()
# words = jieba.lcut(txt)
# nums = {}
# for word in words:
#     if len(word)<=2:
#         continue
#     else:
#         nums[word] =nums.get(word,0) + 1
# items = list(nums.items())
# items.sort(key=lambda x:x[0],reverse=True)
# items.sort(key=lambda x:x[1],reverse=True)
# print(items[0][0])


# tem = input("有格式的温度：\n")
# if tem[-1] in ["F","f"]:
#     C = (eval(tem[0:-1]) - 32) / 1.8
#     print("转换后的温度是{:.2f}C".format(C))
# elif tem[-1] in ["C","c"]:
#     F = 1.8 * eval(tem[0:-1]) + 32
#     print("转换后的温度是{:.2f}F".format(F))
# else:
#     print("错误")

# import turtle as t
# t.setup(800,600,150,200)
# t.penup()
# t.pencolor("green")
# t.pensize(5)
# t.pendown()
# i = 0
# while i <5:
#     t.fd(150)
#     t.right(144)
#     i += 1
#     print(i)
# t.done()
#
# f = open('C:\\Users\\12645\\Documents\\Java\\homework\\myfile.txt','r');
# print(f .readline())
# f.close()
#


# a =[1,2,3,4,5,6,7,8,9]
# b = []
# while(a!= b):
#     for i in a:
#         a.remove(i)
# print("a={}".format(a))


# a =[1,2,3,4,5,6,7,8,9]
# a.clear()
# print(a)

# foo = [1,2]
# foo1 = foo
# foo.append(3)
# print(foo)
# print(foo1)

# for i in range(2):
#     print(i)
#     for i in range(4,6):
#         print(i)

# def writer(fname, text):
#     filepath = "D:/files/" + fname + ".txt"
#     file = open(filepath, "w")
#     file.write(text)
#     file.close()
#     print("finish")
#
# writer(" sss ", "hello world")

import time
from random import random

# a = 1000 * 1000
# hit = 0.0
# start = time.perf_counter()
# for i in range(1, a + 1):
#     x, y = random(), random()
#     dist = pow(pow(x, 2) + pow(y, 2), 0.5)
#     if dist <= 1.0:
#         hit = hit + 1
# pi = 4 * (hit / a)
# end = time.perf_counter() - start
# print(pi)
# print("圆周率：{}".format(pi))
# print("运行时间：{}s".format(end))

# import requests
# import parsel
# url = "https://item.jd.com/100006628190.html#crumb-wrap"
# params = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                   'Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47'}
# respond = requests.get(url, params=params)
# respond.encoding = "GBK"
# Getmytext = respond.text
#
# select = parsel.Selector(Getmytext)
# data = select.xpath('//*[@id="comment-0"]/div[1]/div[2]/p/text()[1]').getall()
# print(data)
