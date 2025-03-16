# _*_ coding : utf-8 _*_
# @Time : 2025/3/15 21:22
# @Author : 田园
# @File : 74-Python_解析_bs4解析麦当劳
# @Project : 73-Python_解析_bs4的基本使用-解析本地文件.py

import urllib.request
from bs4 import BeautifulSoup

url='https://www.mcdonalds.com.cn/product/mcdonalds/hamburgers'

# 反爬
# headers=

# 模拟浏览器向服务器发送请求
response=urllib.request.urlopen(url)
# 获取源码
content=response.read().decode('utf-8')
# print(content)

# 服务器响应的文件生成对象
soup=BeautifulSoup(content,'lxml')

# 麦当劳汉堡页的xpath路径
# //div[@class="row"]//a/span
burgerList=soup.select('.row a>span')
for burgerName in burgerList:
    # print(burgerName.string)
    print(burgerName.get_text())




