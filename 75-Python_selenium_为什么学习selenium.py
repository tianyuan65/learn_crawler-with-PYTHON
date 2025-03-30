# _*_ coding : utf-8 _*_
# @Time : 2025/3/18 10:55
# @Author : 田园
# @File : 75-Python_selenium_为什么学习selenium
# @Project : 74-Python_解析_bs4解析麦当劳.py

import urllib.request

url='https://www.taobao.com/'

# 访问淘宝首页
response=urllib.request.urlopen(url)
content=response.read().decode('utf-8')
# 无法爬取到所有的信息，因为毕竟是模拟浏览器向服务器发送请求，所以服务器方知道用户是在进行爬取操作，返回的结果并不是完整的数据。
print(content)


