# _*_ coding : utf-8 _*_
# @Time : 2025/4/23 16:10
# @Author : 田园
# @File : 82-Python_requests_基本使用
# @Project : 079-Python_selenium_交互.py
import urllib.request
# 引入requests
import requests

# 如何使用？
url='http://www.baidu.com'
# 模拟浏览器向服务器发送请求-请求对象定制的写法
# response=urllib.request.urlopen(url)
# 向服务器发送请求
response=requests.get(url=url)

# 一个类型和六个属性
# 一个类型--与请求对象定制得到的数据类型是HTTPResponse类型不同，这里的变量response的数据类型是Response类型
# print(type(response))   #<class 'requests.models.Response'>

# 六个属性
# .encoding，用于设置编码格式，以防获取的源码中带有乱码
response.encoding='utf-8'
# .text，用于获取网页源码，且是字符串类型的
# print(response.text)
# print(type(response.text))  #<class 'str'>
# .url，返回url地址
# print(response.url) #http://www.baidu.com/
# .content，用于获取网页源码，只不过二进制的，所以实在是没必要，想要获取源码调用text更方便，实在是没必要遭这份罪
# print(response.content)
# .status_code，用于获取响应的状态码
# print(response.status_code) #200
# .headers，用于获取响应的头信息
print(response.headers) #{'Cache-Control': 'private, no-cache, no-store, proxy-revalidate, no-transform', 'Connection': 'keep-alive', 'Content-Encoding': 'gzip', 'Content-Type': 'text/html', 'Date': 'Wed, 23 Apr 2025 11:57:45 GMT', 'Last-Modified': 'Mon, 23 Jan 2017 13:27:36 GMT', 'Pragma': 'no-cache', 'Server': 'bfe/1.0.8.18', 'Set-Cookie': 'BDORZ=27315; max-age=86400; domain=.baidu.com; path=/', 'Transfer-Encoding': 'chunked'}