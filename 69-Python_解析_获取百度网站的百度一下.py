# _*_ coding : utf-8 _*_
# @Time : 2025/3/2 17:04
# @Author : 田园
# @File : 69-Python_解析_获取百度网站的百度一下
# @Project : 68-Python_解析_XPath的基本使用.py

# 1. 获取网页源码
# 2. 解析，解析的是服务器相应的文件，用etree.HTML()
# 3. 打印

# 1. 获取网页源码
import urllib.request

url='https://www.baidu.com'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'}
# 请求对象定制
request=urllib.request.Request(url=url,headers=headers)
# 模拟浏览器向服务器发送请求
response=urllib.request.urlopen(request)
# 获取网页源码
content=response.read().decode('utf-8')
# print(content)

# 解析网页源码，来获取想要的数据，想要百度一下
from lxml import etree
# 解析本地文件调用parse方法，解析服务器响应的文件调用HTML方法，并将需要解析的源码作为参数传进去
tree=etree.HTML(content)

# 获取想要的数据，此处难点：如何书写xpath路径，在chrome快捷键激活XPath Tester后，找到想要的标签，将用标签的id值锁定并用该标签独有的一个属性获取文本内容
# xpath的返回值是一个列表类型的数据，不想看到中括号，也可以添加下标[0]，这样就能获取字符串类型的数据
result=tree.xpath('//input[@id="su"]/@value')
print(result)   #['百度一下']
